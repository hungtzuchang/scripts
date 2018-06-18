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
	
def Lorentzian(Evector,E0,Gamma):
	return Gamma/2/(np.square(Evector-E0)+np.square(Gamma/2))

