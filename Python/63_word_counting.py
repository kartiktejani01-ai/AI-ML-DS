# write a program to count no of words (space)
name = input("Enter Name:")
space = 1
for letter in name:
    if letter == ' ':
        space = space + 1

print(f"No of Words in {name}",space)