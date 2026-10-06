'''
write a program to calculate annual income, Tax, Net income from given monthly income using below tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,000                     40%
    From Rs. 20,00,001 to Rs. 24,00,000	    30%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    10%
    below 12,00,000                          0%
'''
monthly_income = int(input("Enter Your Income"))
annual_income = monthly_income * 12

tex = 0
if annual_income < 1200000:
    tex = 0
    print("Annual Income:", annual_income)

elif annual_income < 1600000:
    tex = (annual_income * 10)/100
    print("Annual Income:", annual_income)

elif annual_income < 2000000:
    tex = (annual_income * 20)/100
    print("Annual Income:", annual_income)

elif annual_income < 24000000:
    tex = (annual_income * 30)/100
    print("Annual Income:", annual_income)

else :
    tex = (annual_income * 40)/100
    print("Annual Income:", annual_income)

print(tex)

net_income = tex - annual_income
print("Net Income:", net_income)