"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a
tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""
num_str=input("Enter your number  :  ")
num_list = num_str.split(",")
print(f"Input Numbers as list : \n {num_list}")
print("Type of above list",type(num_list))
num_tuple = tuple(num_list)
print(f"Input Numbers as Tuple : \n {num_tuple}")
print("Type of above tuple",type(num_list))