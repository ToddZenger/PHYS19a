#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:29:32 2020

@author: Sagar97
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(-10,10,1)

#Using a generic linear equation with some added noise.
y = 1.6*x + 2.4 + 2*np.random.random(len(x))

#linregress returns best fit values.
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("The best fit slope is %.02f +/- %0.02f"%(slope,std_err))

plt.errorbar(x,y,fmt='bo',label='Scatter Plot')
plt.errorbar(x,intercept+slope*x,fmt='-r',label='Best Fit Line')
plt.legend(loc=0)
plt.show()