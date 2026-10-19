# write a program to print multiplication table of 30
'''
    30 X 10 = 300
    30 X 5 = 150
    30 X 4 = 120
    30 X 3 = 90
    30 X 2 = 60
    30 X 1 = 30
'''
no = 30
result = 0
for multipler in range(10,0,-1):
    result = no * multipler
    print(f"{no} X {multipler} = {result}")