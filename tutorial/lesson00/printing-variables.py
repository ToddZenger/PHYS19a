"""
Author: Todd Zenger, Brandeis University
The goal of this script is to use basics of variables
and printing.
"""

#This is a single line comment

"""
Three quotation marks signify a multi-line
comment

Anything that is written inside a comment is ignored
"""

x = 5
y = 2

name = "Todd"

# In python, single and double quotation marks are the same to signify that
# it is a string
message = 'My name is '

print(x) #output: 5
# Everytime we use print, it will output it in a new line
print(x+y) #output: 7

# Now showing two types of division
print("Two types of division: float and integer:")
print(x/y) #output: 2.5
print(x//y) #output: 2

# We can write variables in terms of other variables
print("The modulus is:")
z = x%y
print(z) #output: 1

# A more complicated example:
k=x*(x-z)**y+3
# It follows order of operations:
# 1. Parentheses 
# 2. Exponential
# 3. Multiply/Divide
# 4. Add/subtract
# (Only curved brackets work here! 
# Square, [], and curly, {}, brackets have different meanings!)
# In practice, you should use parentheses to keep organized of your operations
print(k) #output: 83

# We can't mix and match in a printing statement
#print(name + y) #output: TypeError ...
# Notice it doesn't run the print statement with the # in front


# How do we rectify this? 
# We can use commas to combine them together
print(name, y) #output: Todd 2


print(message + name) #output: My name is Todd

# Or, if there is a string we want to directly output, we can write it
print("Hello world!") #output: Hello world!