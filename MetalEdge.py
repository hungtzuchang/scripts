import numpy as np
from scipy.special import gamma

# Equation 6.18 from Ohtaka and Tanabe, PRB 30(8), p4235 (1984)
# D is the energy difference between the Fermi level and the CB minimum
# delta0 is the phase shift of the plane wave due to core hole scattering
# T is temperature
def MetalEdgeAbs(Omega, D, delta0,T):
    zeta0=2*delta0/np.pi-np.power(delta0/np.pi,2)
    prefactor=np.power(D/(2*np.pi*T),zeta0)/D
    preterm=0.5-(Omega/(2*np.pi*T))*1j
    term1=gamma(preterm-zeta0/2)/gamma(preterm+zeta0/2)*gamma(zeta0)
    exponent=np.pi*(zeta0-1)/2
    term=np.real((np.cos(exponent)+np.sin(exponent)*1j)*term1)
    return prefactor*term

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    omega=np.linspace(-0.3,0.3,100)
    plt.figure()
    plt.plot(omega,MetalEdgeAbs(omega,1,0.1,0.005))
    plt.plot(omega,MetalEdgeAbs(omega,1,0.1,0.01))
    plt.plot(omega,MetalEdgeAbs(omega,1,0.1,0.05))
    plt.plot(omega,MetalEdgeAbs(omega,1,0.1,0.1))
    plt.show()
    plt.figure()
    plt.plot(omega,MetalEdgeAbs(omega,1,0,0.005))
    plt.plot(omega,MetalEdgeAbs(omega,1,0.2,0.005))
    plt.plot(omega,MetalEdgeAbs(omega,1,np.pi/4,0.005))
    plt.plot(omega,MetalEdgeAbs(omega,1,np.pi/2,0.005))
    plt.plot(omega,MetalEdgeAbs(omega,1,np.pi,0.005))
    plt.show()
