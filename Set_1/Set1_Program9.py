"""
Read and print number of lines, words and characters in the given file.

"""
word_list=[]
file = open("program9_file")
for f in file:
    word_list.append(f.rstrip("\n").rsplit())
print(word_list)

print("Number of Lines in the file : ",len(word_list))
word_count=0
word_list_2=[]
for element in word_list:
    for word in element:
        word_list_2.append(word)
print(f"Word Count = {len(word_list_2)}")
print(word_list_2)
char_count=0
for element in word_list_2:
    char_count+=len(element)
print(f"Number of Characters = {char_count}")