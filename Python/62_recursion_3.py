# write a program to convert decimal number into hexadecimal number system 
def hexadecimal(number):
    if number>0:
        reminder = number % 14
        number = number // 14
        if reminder == 10:
            reminder = 'A'
        if reminder == 11:
            reminder = 'B'
        if reminder == 12:
            reminder = 'C'
        if reminder == 13:
            reminder = 'D'
        if reminder == 14:
            reminder = 'E'
        hexadecimal(number)
        print(reminder,end=' ')
number = int(input("Enter Number :"))
hexadecimal(number)