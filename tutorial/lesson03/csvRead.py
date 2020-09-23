# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Store the absolute/relative path of your csv file in a string.
InputFile = 'data_1.txt'

PosvsTime = np.loadtxt("data_1.txt", delimiter=",").transpose()

print(PosvsTime)
plt.errorbar(PosvsTime[0],PosvsTime[1],fmt='*b')

#Declare an empty 2D array.
VelvsTime = np.empty((2,0))

#Run a loop from element i=1 to i=n-2.
for i in range(1,len(PosvsTime[0])-1):
    velocity = (PosvsTime[1][i+1]-PosvsTime[1][i-1])/(PosvsTime[0][i+1]-PosvsTime[0][i-1])
    VelvsTime = np.append(VelvsTime,[[PosvsTime[0][i]],[velocity]],axis=1)

#print(VelvsTime)
#plt.errorbar(VelvsTime[0],VelvsTime[1],fmt='-r')

"""
Another quick way to do the numerical differentiation in one step is to skew the two matrixes, take the difference, and divide by 
the time factor. In this case, you need to remember that the time indexing goes from i=1 to i=n-2 and not i=0 to i=n-1.
"""
VelvsTime1 = (PosvsTime[1][2:]-PosvsTime[1][:-2])/(2*0.1)


AccvsTime = np.empty((2,0),float)

for i in range(1,len(VelvsTime[0])-1):
    acceleration = (VelvsTime[1][i+1]-VelvsTime[1][i-1])/(VelvsTime[0][i+1]-VelvsTime[0][i-1])
    AccvsTime = np.append(AccvsTime,[[VelvsTime[0][i]],[acceleration]],axis=1)
    
#print(AccvsTime)
#plt.errorbar(AccvsTime[0],AccvsTime[1],fmt='-g')

bestfitline = stats.linregress(PosvsTime[0],PosvsTime[1])
plt.errorbar(PosvsTime[0],bestfitline[0]*PosvsTime[0]+bestfitline[1],fmt='-r')


plt.xlabel("Time [s]")
plt.show()
