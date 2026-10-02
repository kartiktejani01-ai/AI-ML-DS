'''
fruits ={'apple', 'banana', 'mango', 'kiwi'}
print(fruits) 

fruits.add("orange")
fruits.add("orange")
print(fruits)

fruits.remove("apple")
print(fruits)


set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

print(set1, set2)

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

difference = set1.difference(set2)
print(difference)
'''
countries = ["India", "USA", "Canada", "UK", "Australia", "Germany", "India", "France", 
             "Japan", "Brazil", "USA", "China", "Canada", "India", "Italy", "Germany", "Japan",
               "Australia", "India", "France"]
print(countries)

unique_contries = set(countries)
print(unique_contries)

#convert into list
countries = list(unique_contries)
countries.sort()
print(countries)