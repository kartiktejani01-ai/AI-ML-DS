book = {}
print(book)

book["name"] = "Saurashtr Ni Rasdhar"
book["AuthoeName"] = "Zaverchnd Meghani"
book["price"] = 500

print(book)

#add tupel into dictionary
book['chapter'] = (1, 2, 3, 4)

#add list into dictionary
book["topic"] = ["Index","introduction", "habit", "summery"]
print(book)

#book["chapter":0] = 10
book["topic"][0] = "beginnign"
print(book) 

del book["topic"]
print(book)