import numpy as np
from scipy.signal import fftconvolve
from scipy.stats import norm

def Gauss_conv(v,broadening,spacing):
	gauss_axis=np.arange(-3*v.shape[0]/2,3*v.shape[0]/2)*(spacing)
	vnew=np.r_[v[::-1],v,v[::-1]]
	gauss_Fe3=norm.pdf(gauss_axis,0,broadening)
	Fe3spec=fftconvolve(vnew,gauss_Fe3,'same')*(spacing)
	Fe3spec=Fe3spec[v.shape[0]:2*v.shape[0]]
	return Fe3spec
    
if __name__ == "__main__":
	import matplotlib.pyplot as plt
	x=np.linspace(-10,10,201)
	y=1/(1+np.square(x))
	plt.plot(x,y)
	plt.plot(x,Gauss_conv(y,1,x[1]-x[0]))
	plt.show()
