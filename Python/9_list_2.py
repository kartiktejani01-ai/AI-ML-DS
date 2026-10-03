fruits = ["apple", "banana", "mango",]
print(fruits)

fruits.append("kiwi")
#fruits.append("graph")

#fruits.insert(0, 'pineapple')
#fruits.insert(2, 'charry')

print(fruits)

vegs = ["patoto", "tameto", "cucumber"]
print(vegs)

fruits.extend(vegs)
print(fruits)

vegs.remove("tameto")
print(vegs)

vegs.pop(1)
print(vegs)

vegs.clear()
fruits.sort()
print(vegs)
print(fruits)

fruits.reverse()
print(fruits)

# do not copy
fruits_2 = fruits.copy()
print(fruits, fruits_2)

fruits.clear()
print(fruits)