"""
Author: Todd Zenger, Brandeis University
This program shows lists and introduces loops used
with lists
"""

# First, we can initialize an empty list
x = []

# Now let's start filling it up with a for loop with 5 elements
for i in range(5):
    x.append(i*2)

# Let's see what is inside
# We have two ways to see. Before we do that, let's see everything at once
print("The elements of x is:")
print(x)

# Now, the first way is that we can index and get each item out
print("The elements of x by indexing:")

for i in range(5):
    print(x[i])

# Instead of hard coding the index values, we can have python get it for us
# This makes it more general and easier for us
print("The elements of x by indexing:")

for i in range(len(x)):
    print(x[i])

# The second way is to directly take elements from the list
print("The elements of x by directly getting them:")

for i in x:
    print(i)

# Now let's modify some values of the list
x[3] = 1000

x[1] = -2.1

x[4] = "Ice cream"

print("Changing values in the list:")
print(x)