#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:02:29 2017

@code taken from http://scipy.github.io/old-wiki/pages/Cookbook/SignalSmooth
"""


import numpy as np

def smooth(x,window_len=11,window='hanning'):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal

    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also:

    np.hanning, np.hamming, np.bartlett, np.blackman, np.convolve
    scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError('smooth only accepts 1 dimension arrays.')

    if x.size < window_len:
        raise ValueError('Input vector needs to be bigger than window size')


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError('Window is on of \'flat\', \'hanning\', \'hamming\', \'bartlett\', \'blackman\'')


    s=np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    #print('%d %d\n',int(window_len/2-1),int(window_len/2))
    #print(y.shape)
    return y[int(window_len/2):-int(window_len/2)]


from scipy.stats import norm
from scipy.signal import fftconvolve
def smooth_gaussian(x,step_size,sigma):
    center=3*x.shape[0]/2
    gfilter=norm.pdf(np.arange(-center,center)*step_size,0,sigma)
    xnew=np.r_[x[::-1],x,x[::-1]]
    #gfilter/=np.max(gfilter)
    return step_size*fftconvolve(xnew,gfilter,'same')[x.shape[0]:2*x.shape[0]]
    
from statsmodels.nonparametric.smoothers_lowess import lowess
def smooth_lowess(data):
	filtered = lowess(data, np.arange(0,data.shape[0]), is_sorted=True, frac=0.1, it=0)
	data = filtered[:,1]
	return data
