# write a program to print 1 to 10 using recursion 
# 1 2 3 4 5 6 7 8 9 10 

def printNum(num):
    if num <= 0:
        print(num,end=" ")
        num = num +1
        printNum(num)# recursion 
num = 1
printNum(num) 