"""
Get a list of numbers from users and print the smallest odd number.

"""
try:
    my_list = [int(num) for num in input("Enter your list of numbers:(Use space) \n").split()]
except:
    print("Only Numbers allowed")
odd_list = [num for num in my_list if num%2!=0]
print(f"Minimum of odd values in List = {min(odd_list)}")