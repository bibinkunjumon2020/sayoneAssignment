
"""

Write a program to find all mobile number inside a string.

"""

import re

data = input("Input your String\n")
phone_pattern=re.compile(r'\d\d\d\d\d\d\d\d\d\d')
phone_no=phone_pattern.search(data)
print("Mobile No is : ",phone_no.group())