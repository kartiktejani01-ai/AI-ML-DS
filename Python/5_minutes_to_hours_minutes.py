# write a program to accept minutes from user, then calculate and display hours and remaining
'''
    input : 75 minutes output :  1 hours and 15 minutes
    input : 129 minutes output : 2 hours and 9 minutes
    input : 35 minutes output :  0 hours and 35 minutes
'''
minutes = int(input("Enter minutes:"))
hours = minutes / 60
minutes = minutes % 60

print(f"Hours:{hours}, minutes:{minutes}")
