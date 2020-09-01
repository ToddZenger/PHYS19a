"""
Author: Todd Zenger, Brandeis University
The purpose of this program is to explore
while loops along with some intro to inputs
"""

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