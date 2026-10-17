#example of for loop on list 
#convert all values into positive values 
list = [10,-15,20,-7,45,90,-11,-125]
list_2 = []

for number in list:
    print(number,end=" ")
    if number < 0:
        number = 0 - number
    list_2.append(number)
    print()
    print(list_2)