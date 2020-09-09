"""
Author: Todd Zenger, Brandeis University
The purpose of this program is to explore
while loops along with some intro to inputs
"""

x = 1
while(x<10):
    print("x is {}".format(x))
    x+=1

print()

x = 1
while(x<10):
    print("x is {}".format(x))
    if(x%3==0):
        print("Divisible by 3!")
        break
    x+=1

print()

# We can make an equivalent to a for loop as well
data = [0, 5, 3, 4, 8]
i = 0
while(i<len(data)):
    print("data[{}]={}".format(i, data[i]))
    i+=1

print()

data = [0, 4, 6, 0, 3, 0]
while 0 in data:
    print("data is: {}".format(data))
    data.remove(0)
print("data is: {}".format(data))

print()

"""
Can we find out how many times we need to subtract 3 from 50 to make it
less than or equal to 2?
"""
data = 50
count = 0
while data>2:
    data -= 3
    count += 1
print("It takes {} times to get to less than or equal to 2".format(count))

print()

# More fun stuff: playing with inputs
user_input = input("Enter a number: ")

while(user_input!="1"):
    user_input = input("Enter a number: ")

print("You found the number!")


print("\nEnter 1 for a random number")
print("Enter 2 for a greeting")
print("Enter 3 to leave")
user_input = input("Enter a number: ")

while(True):
    if user_input=="1":
        print("3") # In very loose terms, this is a random number
        # https://xkcd.com/221/
    elif user_input=="2":
        print("Hello!")
    elif user_input=="3":
        print("Goodbye")
        break
    else:
        print("Invalid Choice!")
    
    print("\nEnter 1 for a random number")
    print("Enter 2 for a greeting")
    print("Enter 3 to leave")
    user_input = input("Enter a number: ")