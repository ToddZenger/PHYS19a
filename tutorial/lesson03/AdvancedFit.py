#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 00:37:06 2020

@author: Sagar97
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#y = m*x+b
def LinearFn(x,m,b):
    y = m*x + b
    return y

#y = a*x^2 + b*x + c    
def QuadraticFn(x,a,b,c):
    y = a*x**2 + b*x + c
    return y

#y = ASin(w*t + phi)
def SinFn(x,a,w,phi):
    y = a*np.sin(w*x+phi)
    return y
    
x = np.arange(-1,1,0.1)
y = 5*x**2 - 3*x + 2 + np.random.random(len(x))
popt, pcov = optimize.curve_fit(QuadraticFn,x,y)
print(popt)
print(pcov)

plt.errorbar(x,y,fmt = 'bo',label='Scatter Plot')
plt.errorbar(x,popt[0]*x**2+popt[1]*x+popt[2],fmt='-r',label='Best Fit Curve')

#x = np.arange()