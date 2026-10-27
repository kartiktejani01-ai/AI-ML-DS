number = [10,12,13,14,15]
print(number)

#generate square 
# squared = [] 
# for num in numbers:
#     squared.append(num * num)

squread = map(lambda num : num*num, number)
print(list(squread))

desicion = ["yes","no","yes","no","yes"]
result = map(lambda item: 1 if item == 'yes' else 0, desicion)
print(list(result))