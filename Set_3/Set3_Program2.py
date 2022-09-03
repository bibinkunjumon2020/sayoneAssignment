"""

Get email input from user and check it is valid or not(Output: valid/ Invalid)

"""
import re

def Check(email):
    char = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]"
    if re.match(char,email):
        return True
    return False

my_email = input("Enter email ID")
if(Check(my_email)):
    print("Email ID is Valid ......!")
else:
    print("Invalid Email ID")