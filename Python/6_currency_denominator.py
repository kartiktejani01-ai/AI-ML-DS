# write a program to display denomination of given amount using indian currency.
# start with highest to lowest currency
'''
    Input : Amount :- 888
    500 x 1 = 500 388
    200 x 1 = 200 188
    100 x 1 = 100 088
    050 x 1 = 050 038
    020 x 1 = 020 018
    010 x 1 = 010 008
    005 x 1 = 005 003
    002 x 1 = 002 001
    001 x 1 = 001 000
'''
amount = input("Enter amount")
amount = int(amount)
print("Amount", amount)

five_hd = amount // 500
amount = amount - (five_hd * 500)

two_hd = amount // 200
amount = amount - (two_hd * 200)

one_hd = amount // 100
amount = amount - (one_hd * 100)

fifty = amount // 50
amount = amount - (fifty * 50)

twenty = amount // 20
amount = amount - (twenty * 20)

ten = amount // 10
amount = amount - (ten * 10)

five = amount // 5
amount = amount - (five * 5)

two = amount // 2
amount = amount - (two * 2)

one = amount // 1
amount = amount - (one * 1)

print(f"500 X {five_hd} = {five_hd * 500}")
print(f"200 X {two_hd} = {two_hd * 200}")
print(f"100 X {one_hd} = {one_hd * 100}")
print(f"50 X {fifty} = {fifty * 50}")
print(f"20 X {twenty} = {twenty * 20}")
print(f"10 X {ten} = {ten * 10}")
print(f"5 X {five} = {five * 5}")
print(f"2 X {two} = {two * 2}")
print(f"1 X {one} = {one * 1}")