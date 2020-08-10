"""
Author: Todd Zenger, Brandeis University
The purpose of this code is to calculate the 
basic statistics of a given data set
"""

# I am first importing statistics package for later
import statistics as stat

# Initialize the data set
data = [8, 8.5, 7, 8.9, 8]

# I will create variables to hold the values later
mean = 0
std = 0
stderr = 0

# Calculate the mean
for i in data:
    mean = mean + i

mean = mean / len(data)

# Calculate the standard deviation
for i in data:
    std = std + (i-mean)**2

std = (std/(len(data)-1))**(1/2)

# Calculate the standard deviation of the mean
stderr = std/(len(data)**(1/2))

# Now, let's print them out
print("The mean of the data is: ", mean)
print("The standard deviation is: ", std)
print("The standard deviation of the mean is: ", stderr)

# Now, let's use the statistics library
new_mean = stat.mean(data)

# We have two standrd deviation functions, which one to use?
# Let's output both of them to see...
pstd = stat.pstdev(data)
sstd = stat.stdev(data)

print("Now using the statistics package...")
print("The mean is: ", new_mean)
print("Using pstdev, we get: ", pstd)
print("Using stdev, we get:", sstd)

"""
Running this, you will find that using stdev will give the correct answer and 
pstdev will be a little bit off.

The math behind it is that if you look on line 28: 
std = (std/(len(data)-1))**(1/2)
                      ^
stdev will include this deduction of 1 (shown by the ^) while pstdev will
exclude this
"""