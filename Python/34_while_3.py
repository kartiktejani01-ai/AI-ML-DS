#write a program to calculate compound interest of given amount, rate, year

amount = int(input("Enter amount :"))
rate = float(input("Enter Rate :"))
year = int(input("Enter Year :"))

total_interest = 0

while year >= 1:
    interest = (amount * rate) / 100
    total_interest = total_interest + interest
    amount = amount + interest
    year = year - 1

    print("Total Compound Interest :", round(total_interest,2))
