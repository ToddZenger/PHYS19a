"""
Author: Todd Zenger, Brandeis University
The goal of this program is to give an 
example plot. Commentary of this is located
in lecture slides associated with this code.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0, 1, 2, 3, 4], [1, 2.2, 5, 8, 9.7]])
errs = np.array([0.5, 0.4, 0.3, 0.5, 0.2])
t = np.arange(0, 4, 0.1)
plt.figure()

#plt.plot(data[0], data[1], "ro")
plt.errorbar(data[0], data[1], yerr=errs, fmt="ko",
             barsabove=True, label="Measured")
plt.plot(t, 4.5*np.sin(0.5*t), "--r", label="Expected")

plt.legend(loc="best")

plt.title(r"My plot of data $I=\omega^2$")
plt.xlabel("Time [s]")
plt.ylabel(r"Fake unit $[m^2kg^{-1}]$")

plt.yscale('log')

plt.axis([-0.5, 5, -2, 12])
plt.grid()

plt.show()

