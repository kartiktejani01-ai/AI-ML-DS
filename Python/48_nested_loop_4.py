# write a program to print following pattern 
'''
        1
       0 1
      0 1 0
     1 0 1 0
    1 0 1 0 1
'''

value = 1
for row in range(5,0,-1):
   # print(' ',end=' ')
    for space in range(1,row-2):
        print(' ',end=' ')
        for number in range(6-row,0,-1):
            print(f'{value}',end=' ')
            if value == 1:
                value = 0
            else:
                value = 1
        print(' ')
'''
value = 1
for row in range(5,0,-1): #outer loop 4
    for space in range(-1,row-2): 
        print(' ',end=' ')
    for number in range(6-row,0,-1):
        print(f'{value} ',end=' ')
        if value == 1:
            value = 0
        else:
            value = 1
    print("")
'''