#example of in operator 
number = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(number)
value = 500
isfound = value in number
print(f"is{value} found", isfound)

isfound = value not in number
print(f"is{value} not found", isfound)