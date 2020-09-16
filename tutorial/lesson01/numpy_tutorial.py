"""
Author: Todd Zenger, Brandeis University
The purpose of this program is to tie in between lists and Numpy arrays
and to introduce some concepts of Numpy
"""

import numpy as np
"""
Anytime we want to use Numpy, we must write this on top of our script
"""

# First, let's look at lists once again
x = [4, 9, 12, 13]
y = [2, 4, 8, 15]

# First task, let's increase all elements by 2
for i in range(len(x)):
    x[i] = x[i]+2
    y[i] = y[i]+2

# Now, let's print out the results
print("List x increased by 2 is: {}".format(x))
print("List y increased by 2 is: {}".format(y))

# Second task, let's add x and y together into a new list z

z = []

for i in range(len(x)):
    z.append(x[i]+y[i])

# Remember, that we are using the increased by 2 x and y lists
print("List z is: {}".format(z))

"""
Moral of the story: anytime we want to do something will all or most of the 
elements of a list, we need to create a for loop to help us solve this.

Is there a better way? Yes! Numpy arrays!

Let's solve the previous two tasks with Numpy arrays
"""
print()
xn = np.array([4, 9, 12, 13])
yn = np.array([2, 4, 8, 15])

xn = xn + 2
yn = yn + 2

print("Array x increased by 2 is: {}".format(xn))
print("Array y incraesed by 2 is: {}".format(yn))

# Now let's add them together
zn = xn + yn
print("Array z is: {}".format(zn))

"""
Now, let's get a bit more practical utilizing Numpy's power

The problem: we are given three sets of data and each item in the array
represents a measurement at a certain time. Calculate mean and std at
each time.
"""
print()
data1 = np.array([1, 3, 5, 9])
data2 = np.array([1.4, 2.8, 7, 8.2])
data3 = np.array([0.4, 2.9, 7.6, 7])

mu = (data1 + data2 + data3)/3
print("The mean of this data is: {}".format(mu))

sigma = np.sqrt(((data1-mu)**2+(data2-mu)**2+(data3-mu)**2)/(3-1))
print("The standard deviation is: {}".format(sigma))

"""
Now, some other mathematical things we can do:
"""
print()
# First, we can create arrays in some ascending order
nums = np.arange(10)
print(nums)

# Or, we can sepcify how it counts with (start, stop, steps)
vals = np.arange(0, 3, 0.5)
print(vals)

# There are math functions we can use
sinvals = np.sin(vals)
print(sinvals)
# What use is there for this? It helps us model the expected values

"""
Next, we can go two dimenional. How? We have the array hold arrays!
"""

d = np.array([[1,2],[3,4]])
print()
print("My 2d array d is:")
print(d)

# How do we access items? We can index using [row, column]
print("row 0 column 0: {}".format(d[0,0]))
print("row 0 column 1: {}".format(d[0,1]))
print("row 1 column 0: {}".format(d[1,0]))
print("row 1 column 1: {}".format(d[1,1]))

# If we want all of a certain row or column, we can use slicing
print("The first row is: {}".format(d[0,:]))
print("The second row is: {}".format(d[1,:]))
# Notice, that these columns come out as a 1D array
print("The first column is: {}".format(d[:,0]))
print("The second column is: {}".format(d[:,1]))
