"""
Author: Todd Zenger, Brandeis University
The purpose of this code is to print out
zeros of a quadratic function
"""

# Side note, I realize that you can make a function for this, but I'm
# keeping this very basic for now

a = 1
b = 2.1
c = -3

x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)

print("Solution 1: ", x1)
print("Solution 2: ", x2)

# We also can reduce the length of the output using round()
print("Trimming down the data...")
print("Solution 1: ", round(x1, 2))
print("Solution 2: ", round(x2, 2))
# The value 2 tells us how many decimal places we want to cut down to

# Now let's look at a complex solution
# I'm just copying and pasting the same code as above and modifying c value
print("Now we have complex solutions:")
a = 1
b = 2.1
c = 3

x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)

print("Solution 1: ", x1)
print("Solution 2: ", x2)
"""
In the computer science/engineering world, the complex number
symbol of sqrt(-1) is symbolized by j instead of i
"""
print("Trimming down the data...")
# If you uncomment the two lines below you will get an error
#print("Solution 1: ", round(x1, 2))
#print("Solution 2: ", round(x2, 2))

# We need to print it out piece by piece to trim it down in our case

print("Solution 1: ", round(x1.real, 2), "+", round(x1.imag, 2), "j")
print("Solution 2: ", round(x2.real, 2), "+", round(x2.imag, 2), "j")