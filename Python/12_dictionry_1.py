product = {"name":"IPhone 12", "price":50000, "Weight":250.0, "avaliable":True}
print(product)

print(product["name"])
print(product["price"])

#update value
product["price"] = 30000
product["avaliable"] = False
print(product)

#add new key value
product["Model"] = "12 Pro Max"
print(product)

#delete value
del product["name"]
print(product)