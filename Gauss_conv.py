import numpy as np
from scipy.signal import fftconvolve
from scipy.stats import norm

def Gauss_conv(v,broadening,spacing):
    gauss_axis=np.arange(-3*v.shape[0]/2,3*v.shape[0]/2)*(spacing)
    gauss_Fe3=norm.pdf(gauss_axis,0,broadening)
    Fe3spec=fftconvolve(v,gauss_Fe3,'same')*(spacing)
    return Fe3spec
