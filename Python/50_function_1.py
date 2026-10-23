# example of user defined function
# def function-name(parameter/input):
#   line 1
#   line 2
#   return variable/None
#function create/define
#with return value with argument
def getInterest(amoun,rate,year):
    print("getInterest function executed")

    interest = (amoun*rate*year) / 100
    return interest

# without return without argument
def printLine():
    print("-"*100)
    return None

#execute 
result = getInterest(10000,10,3)
printLine()
print("Simple Interest is ",result)
printLine()

amount = int(input("Enter Amount"))
rate = float(input("Enter rate"))
year = int(input("Enter Year"))
printLine()

result = getInterest(amount,rate,year)
print("Simple Interest is ",result)

