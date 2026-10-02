# write a program to calculate and display simple interest of given amount, rate, year 

amount = float(input("Enter your Amount:"))
rate = float(input("Enetr Rate:"))
year = float(input("Enter Year:"))

simple_intereat = (amount * rate * year)/100
print("Simple Interest:", simple_intereat)