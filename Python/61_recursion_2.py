#convert Desimal number to binary number
def binary(num):
    if num>0:
        reminder = num % 2
        num = num // 2
        binary(num)
        print(reminder,end=" ")
num = 37
binary(num)