import numpy as np
import matplotlib.pyplot as plt

def TaucLorentz(E,E0,Eg,eps1inf,A,C):
    eps2=np.zeros_like(E)
    eps2[E>Eg]=A*C*E0*np.square(E[E>Eg]-Eg)/(E[E>Eg]*(np.square(C*E[E>Eg])+np.square(np.square(E[E>Eg])-E0*E0)))
    #prepare eps1
    aln=np.square(E)*(Eg*Eg-E0*E0)+np.square(Eg*C)-np.square(E0)*(np.square(E0)+2*np.square(Eg))
    aatan=(np.square(E)-E0*E0)*(E0*E0+Eg*Eg)+np.square(Eg*C)
    alpha=np.sqrt(4*E0*E0-C*C)
    gamma2=(E0*E0-C*C/2)
    zeta4=np.square(np.square(E)-gamma2)+np.square(alpha*C)/4
    #eps1
    firstterm=A*C*aln*np.log((E0*E0+Eg*Eg+alpha*Eg)/(E0*E0+Eg*Eg-alpha*Eg))/(np.pi*zeta4*2*alpha*E0)
    secondterm=-A*aatan*(np.pi-np.arctan((2*Eg+alpha)/C)+np.arctan((-2*Eg+alpha)/C))/(np.pi*zeta4*E0)
    thirdterm=2*A*E0*Eg*(np.square(E)-gamma2)*(np.pi+2*np.arctan(2*(gamma2-Eg*Eg)/(alpha*C)))/(np.pi*zeta4*alpha)
    fourthterm=-A*E0*C*(np.square(E)+Eg*Eg)*np.log(np.abs(E-Eg)/(E+Eg))/(np.pi*zeta4*E)
    fifthterm=2*A*E0*C*Eg*np.log(np.abs(E-Eg)*(E+Eg)/np.sqrt(np.square(E0*E0-Eg*Eg)+np.square(Eg*C)))/(np.pi*zeta4)
    eps1=eps1inf+firstterm+secondterm+thirdterm+fourthterm+fifthterm
    n=np.sqrt((np.sqrt(np.square(eps1)+np.square(eps2))+eps1)/2)
    k=np.sqrt((np.sqrt(np.square(eps1)+np.square(eps2))-eps1)/2)
    Abs=k*E
    return Abs,n,k
