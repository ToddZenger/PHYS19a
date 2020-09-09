"""
Author: Todd Zenger, Brandeis University
The purpose of this code is to figure out how to bring 
the mean of two values of a large range down
"""
import numpy as np

# Method 1: simply use variables to continuously check

# Our two values
x1 = 3
x2 = 555

# The number of times we add 2
n = 0

# We want this loop to run while the mean is greater than 10
while ((x1+x2+2*n)/(2+n)>10):
    n+=1 # If it fails, increase n by 1

print("Method 1: added {} times".format(n))

# Method 2: We can use Numpy to do much of the heavy work for us

data = np.array([3,555])

while(np.mean(data)>10):
    data = np.append(data,2) # This sticks a value of 2 at the end of the array

n_np = data.shape[0] - 2 # This finds the length and we take out the values of 3 and 555

print("Method 2: added {} times".format(n_np))

"""
Discussion:
Does this fit expected results mathematically?

We solve with the definition of the mean:

(3+555+2*N)/(N+2) <= 10

Solving this gives N as 67.25. When we round up, this gives 68, which
is exactly what we we got.
"""