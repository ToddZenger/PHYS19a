"""
Author: Todd Zenger, Brandeis University
This program introduces more about logical
statements and if statements
"""

# First, let's practice with some logical statements

# Let's ask it some questions
print("Is 5 less than 3? {}".format(5<3)) # Is 5 less than 3? Answer: False (No)

print("Is 5 greater than 3? {}".format(5>3)) # Is 5 greater than 3? Answer True (Yes)

print("Is 5 greater than or equal to 3? {}".format(5>=3)) # Is 5 greater than or equal to 3? Answer: True


print("Is 5 greater than 5? {}".format(5>5)) # Is 5 greater than 5? Answer: False


print("Is 5 greater than or equal to 5? {}".format(5>=5)) # Is 5 greater than or equal to 5? Answer: True


print("Is 5 equal to 5? {}".format(5==5)) # Is 5 equal to 5? Answer: True


print("Is 5 equal to 3? {}".format(5==3)) # Is 5 equal to 3? Answer: False


print("Is 5 not equal to 3? {}".format(5!=3)) # Is 5 not equal to 3? Answer: True


print("Is Hello equal to Hello? {}".format("Hello" == 'Hello')) # Do these strings match? Answer: True

# Now let's complicate it by joining statements together

print("\n~~~Now joining statements together~~~\n")

# First, let's look at cases with straight True and False statements
a = True # Our True variable
b = False # Our False variable

print("a is {}".format(a))
print("b is {}".format(b))

print("a and a: {}".format(a and a)) # True and True. Answer: True
print("a and b: {}".format(a and b)) # True and False. Answer: False
# Note: swapping a and b here does not matter
# i.e. order in placing in these statements do not matter
print("b and b: {}".format(b and b)) # False and False. Answer: False

# Now or statmenets
print("a or a: {}".format(a or a)) # True or True. Answer: True
print("a or b: {}".format(a or b)) # True or False. Answer: True
print("b or b: {}".format(b or b)) # False or False. Answer: False

# We can invert as well:
print("not a or b: {}".format(not(a or b))) # Not True or False. Answer: False
print("not b or b: {}".format(not(b or b))) # Not False or False. Answer: True

# We are now ready to use these answers to have Python act as 
# a gatekeeper to blocks of code

if(a):
    print("Hello!")
else:
    print("Goodbye!")
# We will have Hello! printed out
if(b):
    print("Hello!")
else:
    print("Goodbye!")
# We will have Goodbye! printed out


print("\n~~~Now let's look at more practical use of if-else~~~\n")

data = 3
print("\nData is: {}".format(data))
if(data>10):
    print("Too big!")
elif(data <=10 and data > 7):
    print("Just right!")
elif(data <=7 and data > 3):
    print("Almost!")
else:
    print("Too small!")
