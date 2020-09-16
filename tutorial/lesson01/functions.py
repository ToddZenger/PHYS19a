"""
Author: Todd Zenger, Brandeis University
The purpose of this program is to show some
basics of functions.
"""

"""
First, we can put something in, and get a value out

NOTICE: you are responsible to figure out what data type you are
passing into the function and what type you are spitting out
"""
def f(x):
    y = 3*x + 2
    return y

# To get this value, we define it like any other variable
g = f(4) # g is now equal to 14

"""
Passing in variables is fine as well.
It doesn't matter if we used x as an argument
for the funciton.
"""
x = 2
h = f(x) # h is now equal to 8


"""
Now, we can have the function give out multiple values.
"""

def funcs(x):
    y = 3*x - 2
    z = 3*(x**2) - 2*x
    
    # Each value we want to return, we seperate with a comma
    return y, z

"""
There are two ways to extract a value from a function:
1) Either we define a new variable for each return value
We can then use each one as a variable like we normally do
"""

j, k = funcs(4) # j is 10 and k is 40

"""
2) We can define a single variable that will hold all return
values. It will then become a tuple, which is like a list
that we cannot modify. Then to get each value, we just index
like we would for a list that has the size of the number
of return values we have
"""

n = funcs(3)
"""
Here, n is (7,21)
So, n[0] is 7
and n[1] is 21
"""

"""
Next, we can pass in multiple values for the function to process
"""

def mulfunc(x, y, message):
    print(message) #We are allowed to do other operations like normal

    return (x+3*y) # We don't have to create a variable just to return

d = mulfunc(2, 4, "Hello!") # d is 14


"""
Final thing (at least for now) about functions, all the arguments we
pass in don't always have to be set everytime. We can make a 
default value and choose whenever we want to set them
"""

def fixedfunc(x, y, mu=25, chi=3):
    return x*y - mu**chi

"""
First, we keep all default values
"""
q = fixedfunc(2, 5) # q is -15615

"""
We can change the default values as well
"""
e = fixedfunc(4, 6, mu=5, chi=2) # e is -1

"""
Or some of the default values as well
"""
i = fixedfunc(1, 9, mu=2) # i is 1