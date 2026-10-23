# write a program to print following pattern 
'''
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

    1 
   2 1 
  3 2 1 
 4 3 2 1 
5 4 3 2 1 
'''

for row in range(5,0,-1):
    for space in range(-1,row-2):
        print(' ',end='')

    for number in range(6-row,0,-1):
        print(number,end=' ')
    print("")

