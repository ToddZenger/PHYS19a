"""
Author: Todd Zenger, Brandeis Univerity
This script explores Numpy's broadcasting
feature
"""
import numpy as np

# The matrix we are asked to make is
m = np.array([[0,1], [2, 3], [4,5]])

# Now, let's have two other arrays
a = np.array([8, 9]) # Row array
b = np.array([[11], [12], [13]])

# Now, I will just add them here, but see similar will happen
# if you try to subtract, divide, or multiply them

ma = m + a
print("m + a gives us:")
print(ma)

mb = m + b
print("m + b gives us:")
print(mb)

"""
If we try a = np.array([[8],[9]])
or b = np.array([11,12,13]) we will get an error!
"""

"""
So what is happening behind the scenes?
Let's look at what actually happens with ma:

m + a -> 
[[0,1],     [8,9]
 [2,3],  +        
 [4,5]]
->[[0,1],     [[8,9],
  [2,3],  +    [8,9],      
  [4,5]]       [8,9]]

This is what happens when broadcasting occurs. It "streches" the mismatched
array to make it fit
"""