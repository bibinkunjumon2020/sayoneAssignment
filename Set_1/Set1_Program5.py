"""

Write a program to generate and print another tuple whose values are
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

"""
given_set = (1,2,3,4,5,6,7,8,9,10)
new_set=[]
for element in given_set:
    if(element%2==0):
        new_set.append(element)
print(f"Even numbers as tuple : \n {tuple(new_set)}")
