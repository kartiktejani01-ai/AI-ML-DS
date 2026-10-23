# write a program to print following pattern 
'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
for row in range(5,0,-1):
    for number in range(0,row):
            print(number+1,end=" ")
    print()