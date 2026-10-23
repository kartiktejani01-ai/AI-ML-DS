#Arbitrary Argument functions
#create function that return sum of all the values 
def getsumAverage(*number):
    sum = 0
    for num in number:
        print(num,end=' ')
        sum = sum + num
    print("")
    average = sum / len(number)
    return sum , average
result = getsumAverage(10,20,30)
print(f"sum & Average of Value ={result}")
result = getsumAverage(10,40,50,60)
print(f"Sum & Average of Value ={result}")
