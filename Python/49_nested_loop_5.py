# write a program to find out whether give number is armstrong number or not
# input 153
#process : 1x1x1 5x5x5 3x3x3 -> 1 + 125 + 27 = 153(armstrong number)
#input 1634
#process : 1x1x1x1 6x6x6x6 3x3x3x3 4x4x4x4 -> 1 + 1296 + 81 + 256 = 1634

num = 153
length = len(str(num))
reminder = num %10
total = 0
power = 1
for i in range(0,length):
    power = power * reminder
total = total+power
num = num //10
reminder = num % 10
power = 1
for i in range(0,length):
    power = power * reminder
total = total+power
print(total)
num = num // 10
reminder = num % 10
power = 1
for i in range(0,length):
    power = power * reminder
total = total+power
print(num)