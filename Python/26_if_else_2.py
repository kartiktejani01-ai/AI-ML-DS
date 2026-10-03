# write  a program to accept 24 hours format time from user and convert it into 12 hours format time 
'''
    input : 18 hours output : 6 PM 
    input : 09 hours output : 9 AM 
'''

hours = int(input("Enter Hours"))

if hours<=12:
    print(f"{hours} AM")

else :
    hours = hours - 12
    print(f"{hours} PM")
