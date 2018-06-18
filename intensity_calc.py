#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 12:59:21 2017

@author: htchang
"""
import numpy as np
def intensity_calc(E_meas, sigma_x, sigma_y, index_of_refraction, pulse_duration, central_mode_ratio, relative_peak_power=1):
    ''' E_meas in microjoule and sigma in micron, pulse_duration in fs
        Returns vacuum intensity, sample intensity (in W/cm^2) vacuum fluence (J/cm^2), mode size,'''
    tau=pulse_duration # pulse duration in Femtoseconds
    n=index_of_refraction #4.763 # index of refraction
    waist_x=2*sigma_x #*2.04 #FWHM*sqrt(2)/sqrt(log(2))/2;
    waist_y=2*sigma_y #*2.04; #FWHM*sqrt(2)/sqrt(log(2))/2;
    E=E_meas*1.11/1E6/relative_peak_power*central_mode_ratio #(1-(n-1)^2/(n+1)^2) #E_meas*(1+((1.46-1)/(1.46+1))^2)/1E6/relative_peak_power;
    I=np.sqrt(16*np.log(2)/np.pi**3)*E/((waist_x/1E6)*(waist_y/1E6)*(tau/1E15))/(100*100)
    I_int=n*(2/(1+n))**2*I
    fluence=2*E/(np.pi*(waist_x/1E6)*(waist_y/1E6))/(100*100)
    return I,I_int,fluence,waist_x*waist_y*np.pi