# example of for loop 
#findout maximum value and its position in list 
list = [10,15,200,7,45,90,-11,125]
max = list[0]
position = 0

for index, value in enumerate(list):
    if max>value:
        max = value
        position = index
print(f"Maximum value {max} and position {position}")