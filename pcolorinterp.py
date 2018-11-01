import numpy as np
from scipy.interpolate import interp2d

def pcolorinterp(xin,yin,zin,xminmax,yminmax,xsteps=101,ysteps=101):
    xout=np.linspace(xminmax[0],xminmax[1],xsteps)
    yout=np.linspace(yminmax[0],yminmax[1],ysteps)
    f=interp2d(xin,yin,zin,kind='cubic')
    zout=f(xout,yout)
    return xout,yout,zout

if(__name__=='__main__'):
    x=np.linspace(0,10,200)
    y=np.linspace(0,10,200)
    z=np.zeros(200)
    print(pcolorinterp(x,y,z,[0,10],[0,10])[2].shape)

