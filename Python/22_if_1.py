#write a program to findout profit or loss amount from given purchase and sales price of product
#task 
# also calculate and display profit or loss percentage 

purchase_price = int(input("Enter purchase Price:"))
sales_price = int(input("Enter sales Price:"))

deffrence = sales_price - purchase_price

if deffrence>0:
    print(deffrence, "is your Profit.")
if deffrence<0:
    print(deffrence, "is your Loss.")


if deffrence>0:
    profit_percentage = (deffrence / purchase_price) / 100
    print("profit Percentage", profit_percentage, "%")
if deffrence<0:
    loos_percentage = (deffrence / purchase_price) / 100
    print("loos Percentage", loos_percentage, "%")

print("Good Bey")
