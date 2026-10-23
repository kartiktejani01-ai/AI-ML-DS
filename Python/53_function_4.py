#Arbitrary Argument functions
#create function that return sum of all the values 
def getsum(*number): # *means numbers is tuple(read only list) 
    sum = 0
    for num in number:
        print(num,end=' ')
        sum = sum + num
    print("")
    return sum

sum = getsum(10,2,3)
print(f"sum of Value={sum}")
sum = getsum(100,200)
print(f"Sum of Value={sum}")
sum = getsum(100)
print(f"Sum of Value={sum}")