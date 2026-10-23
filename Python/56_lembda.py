# example of lambda function
getIntrest = lambda amount,rate,year : (amount * rate * year)/100
CeltoFeren = lambda celsius : (celsius * (9/5) + 32)

amount = int(input("Enter Amount :"))
rate = float(input("Enter Rate :"))
year = float(input("Enter Year :"))

celsius = float(input("Enter Tempurachure in Celisus :"))

interest = getIntrest(amount,rate,year)
print(f"Interest = {interest:.2f}")

Ferenheit = CeltoFeren(celsius)
print(f"Fenrenhit = {Ferenheit:.2f}")
