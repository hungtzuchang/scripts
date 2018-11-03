#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:42:17 2017

@author: htchang
"""

import numpy as np

def FanoProfile(Evector,E0,Gamma,q):
    Evectornew=(Evector-E0)*2/Gamma
    return (np.square(Evectornew+q)/(1+np.square(Evectornew)))

def FanoProfileNorm(Evector,E0,Gamma,q):
    Evectornew=(Evector-E0)*2/Gamma
    return (np.square(Evectornew+q)/(1+np.square(Evectornew))-1)*Gamma/2/(q*q-1)/np.pi

def Lorentzian(Evector,E0,Gamma):
	return Gamma/2/(np.square(Evector-E0)+np.square(Gamma/2))

def LorentzianNorm(Evector,E0,Gamma):
	return Gamma/2/(np.square(Evector-E0)+np.square(Gamma/2))/np.pi
#Consult Ott et al. Science 340 p716 (2013)
def FanoUnifiedPhase(Evector,E0,Gamma,phi):
	phi=(phi + np.pi) % (2 * np.pi ) - np.pi
	Evectornew=(Evector-E0)*2/Gamma
	if(np.abs(phi)<1e-6):
		return Gamma/2/(np.square(Evector-E0)+np.square(Gamma/2))
	else:
		q=-1./np.tan(phi/2)
		return (np.square(Evectornew+q)/(1+np.square(Evectornew)))

def FanoUnifiedPhaseNormalize(Evector,E0,Gamma,phi):
	phi=(phi + np.pi) % (2 * np.pi ) - np.pi
	Evectornew=(Evector-E0)*2/Gamma
	q=-1./np.tan(phi/2)
	#print(q)
	v=(np.square(Evectornew+q)/(1+np.square(Evectornew)))
	return v#/np.max(v)
	#if(np.abs(phi)<1e-8):
	#	v=Gamma/2/(np.square(Evector-E0)+np.square(Gamma/2))
	#	return v#/np.max(v)
	#else:
	#	q=-1./np.tan(phi/2)
	#	print(q)
	#	v=(np.square(Evectornew+q)/(1+np.square(Evectornew)))
	#	return v#/np.max(v)

def q2phase(q):
    return 2*np.angle(q-1j)

def phase2q(phi):
    return -1./np.tan(phi/2)

if __name__=='__main__':
	import matplotlib.pyplot as plt
	x=np.linspace(-10,10,100)
	plt.plot(x,FanoUnifiedPhaseNormalize(x,0,1,-0.1))
	plt.plot(x,FanoUnifiedPhaseNormalize(x,0,1,0))
	#plt.plot(x,FanoUnifiedPhaseNormalize(x,0,0.1,1e-6))
	plt.plot(x,FanoUnifiedPhaseNormalize(x,0,1,0.1))
	#plt.plot(x,FanoUnifiedPhaseNormalize(x,0,0.1,0.5))
	#plt.plot(x,FanoUnifiedPhaseNormalize(x,0,0.1,1))
	plt.plot(x,FanoUnifiedPhaseNormalize(x,0,1,np.pi))
	plt.show()
