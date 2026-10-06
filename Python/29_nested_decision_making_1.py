# write a program to findout & display how many days given month has (make sure user give valid month)
'''
    1,3,5,7,8,10,12 = > 31 day
    4,6,9,11 => 30 day
    2 => 28/29 days
'''
month = int(input("ENter Month bitween(1 to 12)"))
if month<1 or month>12:
    print("Month is no Valid")
else:
    if month == 2:
        print("this Month has 28/29 Days")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("This Month Has 31 Days")
    if month == 4 or month == 6 or month == 9 or month == 11:
        print("This Month has 30 Days")