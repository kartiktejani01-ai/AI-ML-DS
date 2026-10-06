#write a program to print following series 
# 1	  2	4	7	11	16	22 ... 100

num = 1
gap = 1

while num < 100:
    print(num,end=" ")
    num = num + gap
    gap = gap + 1