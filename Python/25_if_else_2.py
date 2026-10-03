# write  a program to accept 24 hours format time from user and convert it into 12 hours format time 
'''
    input : 18 hours output : 6 PM 
    input : 09 hours output : 9 AM 
    task (without using nested decision making)
    input : 12 hours output : 12 noon
    input : 24 hours output : 12 midnight
'''
hours = int(input("Enter Hours"))

if  hours == 12:
    print("Noon")
    exit()

if  hours == 24:
    print("Midnight")
    exit()

if hours<=12:
    print(f"{hours} AM")

else :
    hours = hours - 12
    print(f"{hours} PM")

