fruits = ("apple", "banana", "orange", "kiwi", "chery")
print(fruits)

value = input("Enter your favourite fruits:")
isfound = value in fruits
print(f"is{value} found", isfound)

isfound = value not in fruits
print(f"is{value} not founf", isfound)