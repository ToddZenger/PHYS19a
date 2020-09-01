"""
Author: Todd Zenger, Brandeis Univeristy
The goal of this program is to introduce 
logical statements and if statements
"""
import statistics as stats

x = "Hello" == 'Hello'
print("x is {}".format(x))

print("Data set 1")

data = [2,10,5,9]
data_mean = stats.mean(data)
print("Mean is: {}".format(data_mean))

if data_mean>8:
    print("Too Big!")
elif data_mean<=8 and data_mean > 6:
    print("Just right!")
else:
    print("Too big!")

print("Data set 2")
    
data = [2,1,5,9]
data_mean = stats.mean(data)
print("Mean is: {}".format(data_mean))

if data_mean>8:
    print("Too Big!")
elif data_mean<=8 and data_mean > 6:
    print("Just right!")
else:
    print("Too small!")

print("Data set 3")

data = [12,10,5,9]
data_mean = stats.mean(data)
print("Mean is: {}".format(data_mean))

if data_mean>8:
    print("Too Big!")
elif data_mean<=8 and data_mean > 6:
    print("Just right!")
else:
    print("Too big!")