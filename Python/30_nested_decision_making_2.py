# write a program to findout & whether given year is leap year or not
year = int(input("Enter Year"))

reminder1 = year % 4
reminder2 = year % 100
reminder3 = year % 400

if reminder1 == 0 and reminder2 != 0:
    print("This is Leap Year")
else :
    if reminder2 == 0 and reminder3 == 0:
        print("This is Leap Year")
    else:
        print("This is not Leap year")