def getMerit(math,science,english,gujrati,hindi,social):
    print(f"Math={math}, Science={science}, English={english}, Gujrati={gujrati}, Hindi={hindi}, Social={social}")
    total = math + science + english  
    return total
m = int(input("Enter Math Marks :"))
s = int(input("Enter Science Marks :"))
e = int(input("Enter English Marks :"))
g = int(input("Enter Gujrati Maeks :" ))
h = int(input("Enter Hindi Marks :"))
so = int(input("Enter Social Marks :"))

# Worng way of calling function 
total = getMerit(m,s,e,g,h,so)
print("Total ", total)


