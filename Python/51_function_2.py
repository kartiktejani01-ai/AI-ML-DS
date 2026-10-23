# function that Without return value with argument 
def printLetter(letter,times):
    print(letter*times)
    return None

# With Return Value Withour Argument
def getpi():
    #Local Variable
    pi = 22/7
    return pi

#Function Exicute
printLetter('@',50)
print("The Eacylearn Academy. ")
printLetter('~',40)
print("Bhavnagar")
printLetter('-',30)

pi = getpi()
print("Value of Pi ",round(pi,2))