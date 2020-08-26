"""
Author: Todd Zenger, Brandeis Univeristy
The goal of this program is to introduce 
logical statements and if statements
"""
import numpy as np

x = "Hello" == 'Hello'
print("x is {}".format(x))

print("Data set 1")

data = np.array([2,10,5,9])
print("Mean is: {}".format(data.mean()))

if data.mean()>8:
    print("Too Big!")
elif data.mean()<=8 and data.mean() > 6:
    print("Just right!")
else:
    print("Too big!")

print("Data set 2")
    
data = np.array([2,1,5,9])
print("Mean is: {}".format(data.mean()))

if data.mean()>8:
    print("Too Big!")
elif data.mean()<=8 and data.mean() > 6:
    print("Just right!")
else:
    print("Too small!")

print("Data set 3")

data = np.array([12,10,5,9])
print("Mean is: {}".format(data.mean()))

if data.mean()>8:
    print("Too Big!")
elif data.mean()<=8 and data.mean() > 6:
    print("Just right!")
else:
    print("Too big!")