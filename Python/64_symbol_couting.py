# write a program to count symbols
Name = input("Enter Name")
symbols = symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
                     '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>',
                       '/', '?', '`', '~']
count = 0
for letter in Name:
    if letter in symbols:
        count = count + 1 
    print(f"Number of Symbols {count}")