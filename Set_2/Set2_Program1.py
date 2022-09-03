"""

Let 'a' be the list of users who likes a post! I want to get displayed as below.
eg 1 :-       a = []
Output :      Nobody likes This
eg 2 :-       a = ['Alice']
Output :      Alice likes This
eg 3 :-       a = ['Alice','Bob']
Output :      Alice and Bob likes This
eg 4 :-       a = ['Alice', 'Bob', 'Charls']
Output :      Alice, Bob and Charls likes This
eg 5 :-       a = ['Alice', 'Bob', 'Charls','Denny']
Output :      Alice, Bob and 2 others likes This
eg 6 :-       a = ['Alice', 'Bob', 'Charls','Denny','Emely']
Output :      Alice, Bob and 3 others likes This

"""
like_list=[name for name in input("Who liked this post:(Use space) \n").split()]
print("People who liked the post are :",like_list)
count=len(like_list)
if count==0:
    print("Nobody likes This")
elif count==1:
    print(f"{like_list.pop()} likes This")
elif count==2:
    print(f"{like_list[0]} and {like_list[1]} like This")
elif count==3:
    print(f"{like_list[0]},{like_list[1]} and {like_list[2]} like This")
elif count==4:
    print(f"{like_list[0]},{like_list[1]} and 2 others like This")
else:
    print("Not more than 4 names")

