import numpy as np

def FTSpectrum(y,zeropad=4,backward=False):
    ynew=np.append(y,np.zeros(zeropad*y.shape[0],dtype=np.complex))
    #Eaxis=2*np.pi/tspan*np.arange(0,y.shape[0])
    #Eaxis-=np.average(Eaxis)
    if(backward==True):
        yfft=np.fft.ifftshift(np.fft.ifft(ynew))
    else:
        yfft=np.fft.fftshift(np.fft.fft(ynew))

    return yfft

def FTAxis(dt,nsteps):
    Eaxis=2*np.pi/dt*np.linspace(0,1,nsteps,endpoint=False)
    return Eaxis-np.average(Eaxis)
