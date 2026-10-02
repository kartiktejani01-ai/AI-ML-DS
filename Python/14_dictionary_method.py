center = {"name":"Kartik", "Year":2013, "city":"Bhavnager", "Pincode":364260}
print(center)

center_2 = center.copy()
print(center_2)

#remove key value dictionary
center_2 = center_2.clear()
print(center_2)

print("key", center.keys())

print("value", center.values())
print("Dictionary as a item", center.items())
print("Person Name", center.get("name", "notfound"))
print("Kartik Email:", center.get("Email", "notfound"))

center.pop('Pincode')
print(center)

center.update({'owner':"Tejnai"})
print(center)

#creat list
student = ["name", "age", "gender", "email", "dob"]
print(student)

#creat dictionary using list
dishant = dict.fromkeys("student")
Kartik = dict.fromkeys("student")
Hrshali = dict.fromkeys("student")

print(dishant, Kartik, Hrshali)

dishant["name"] = "dishant"
dishant["age"] = 21
dishant["Gender"] = "Male"

print(dishant)


