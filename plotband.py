# This was written by Levi Lentz for the Kolpak Group at MIT
# Modified by Hung-Tzu Chang at Berkeley
# This is distributed under the MIT license
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import sys

#This function extracts the high symmetry points from the output of bandx.out
def Symmetries(fstring):
    f = open(fstring,'r')
    x = np.zeros(0)
    for i in f:
        if "high-symmetry" in i:
            x = np.append(x,float(i.split()[-1]))

    f.close()
    return x
# This function takes in the datafile, the fermi energy, the symmetry file, a subplot, and the label
# It then extracts the band data, and plots the bands, the fermi energy in red, and the high symmetry points
def GetBands(datafile):
    z = np.loadtxt(datafile) #This loads the bandx.dat.gnu file
    x = np.unique(z[:,0]) #This is all the unique x-points
    bands = []
    bndl = len(z[z[:,0]==x[1]]) #This gives the number of bands in the calculation
    for i in range(0,bndl):
        bands.append(np.zeros([len(x),2])) #This is where we storre the bands

    for i in range(0,len(x)):
        sel = z[z[:,0] == x[i]]  #Here is the energies for a given x
        test = []
        for j in range(0,bndl): #This separates it out into a single band
            bands[j][i][0] = x[i]
            bands[j][i][1] = sel[j][1] #np.multiply(sel[j][1],13.605698066)

    return bands,x

def PlotBands(datafile,fermi,symmetryfile,Emin,Emax,xlabels,savefilename):
    bands,x=GetBands(datafile)
    Fermi = float(fermi)
    axis = [min(x),max(x),Emin, Emax]
    for i in bands: #Here we plots the bands
        plt.plot(i[:,0],i[:,1]-Fermi,color="black")

    temp = Symmetries(symmetryfile)
    for j in temp: #This is the high symmetry lines
        x1 = [j,j]
        x2 = [axis[2],axis[3]]
        plt.plot(x1,x2,'--',lw=0.55,color='black',alpha=0.75)

    plt.plot([min(x),max(x)],[0,0],color='red')
    plt.xticks(temp,xlabels)
    plt.ylabel('$E-E_F$ [eV]')
    plt.ylim([axis[2],axis[3]])
    plt.xlim([axis[0],axis[1]])

def PlotBandsDOS(bandfile,DOSfile,fermi,symmetryfile,Emin,Emax,xlabels,savefilename):
    bands,x=GetBands(bandfile)
    Fermi = float(fermi)
    axis = [min(x),max(x),Emin, Emax]
    temp = Symmetries(symmetryfile)
    dos=np.loadtxt(DOSfile,skiprows=1).T
    #print(dos.shape)
    with plt.style.context(('presentation')):
        fig = plt.figure()
        #ax1 = fig.add_subplot(1,2,1, aspect = 'equal')
        #ax2 = fig.add_subplot(1,2,2, aspect = 'equal', sharey = ax1)
        f, (ax1, ax2) = plt.subplots(1,2, sharey=True,tight_layout=True,figsize=(10,7),gridspec_kw={'width_ratios':[6,1],'hspace':-0.5})
        for i in bands: #Here we plots the bands
            ax1.plot(i[:,0],i[:,1]-Fermi,color="black")

        for j in temp: #This is the high symmetry lines
            x1 = [j,j]
            x2 = [axis[2],axis[3]]
            ax1.plot(x1,x2,'--',lw=0.55,color='black',alpha=0.75)

        #ax1.plot([min(x),max(x)],[0,0],color='red')
        ax1.set_xticks(temp)
        ax1.set_xticklabels(xlabels)
        ax1.set_ylabel('$E-E_F$ [eV]')
        plt.ylim([axis[2],axis[3]])
        ax1.set_xlim([axis[0],axis[1]])
        plt.setp(ax2.get_yticklabels(), visible=False)
        if(dos.shape[0]==2):
            ax2.plot(dos[1],dos[0])
        else:
            ax2.plot(dos[1],dos[0]-Fermi,label='up')
            ax2.plot(dos[2],dos[0]-Fermi,label='down')

        ax2.set_xticks([])
        ax2.legend()
        plt.subplots_adjust(wspace = -.000)
    if(savefilename!=None):
        plt.savefig(savefilename,bbox_inches='tight',transparent=True)
    plt.show()
            #ax2.plot(dos[3],dos[0],label='total')


def bndplot(datafile,fermi,symmetryfile,subplot,label):
    z = np.loadtxt(datafile) #This loads the bandx.dat.gnu file
    x = np.unique(z[:,0]) #This is all the unique x-points
    bands = []
    bndl = len(z[z[:,0]==x[1]]) #This gives the number of bands in the calculation
    Fermi = float(fermi)
    axis = [min(x),max(x),Fermi - 4, Fermi + 4]
    for i in range(0,bndl):
        bands.append(np.zeros([len(x),2])) #This is where we storre the bands

    for i in range(0,len(x)):
        sel = z[z[:,0] == x[i]]  #Here is the energies for a given x
        test = []
        for j in range(0,bndl): #This separates it out into a single band
            bands[j][i][0] = x[i]
            bands[j][i][1] = sel[j][1] #np.multiply(sel[j][1],13.605698066)

    print(len(bands))
    for i in bands: #Here we plots the bands
        subplot.plot(i[:,0],i[:,1],color="black")

    temp = Symmetries(symmetryfile)
    for j in temp: #This is the high symmetry lines
        x1 = [j,j]
        x2 = [axis[2],axis[3]]
        subplot.plot(x1,x2,'--',lw=0.55,color='black',alpha=0.75)

    subplot.plot([min(x),max(x)],[Fermi,Fermi],color='red',)
    subplot.set_xticklabels([])
    subplot.set_ylim([axis[2],axis[3]])
    subplot.set_xlim([axis[0],axis[1]])
    subplot.text((axis[1]-axis[0])/2.0,axis[3]+0.2,label,va='center',ha='center',fontsize=20)
