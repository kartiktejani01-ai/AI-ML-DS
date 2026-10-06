'''
write a program to findout person's obesity level using B.M.I(body to mass index) technique. and display obesity level of person as below rule 
obesity level 
    Extremely Obese: BMI 35.0 and above
    Obese: BMI between 30.0  34.9
    Overweight: BMI between 25.0  29.9
    Normal: BMI between 18.5 to 24.9
    Underweight: BMI less than 18.5
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    bmi = weight(Kg ) / (height_in_meter * height_in_meter)
    
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into total inch 
    3   total inch convert into meter 
    5   calculate BMI 
    5   calculate & display person obesity level
'''
weight = float(input("Enter your Weight"))
foot = float(input("Enter Hight in foot"))
inches = float(input("Enter hight in inch"))

#total inches cal.
total_inches = (foot * 12) + inches

#convert inches to meter
meter = total_inches / 39.37

#calculate BMI
bmi = weight / (meter * meter)

print("BMI", bmi)

'''
    Extremely Obese: BMI 35.0 and above
    Obese: BMI between 30.0  34.9
    Overweight: BMI between 25.0  29.9
    Normal: BMI between 18.5 to 24.9
    Underweight: BMI less than 18.5
'''

if bmi>=25.0 and bmi<=29.9:
    print("you are overweight, eat less and walk more")
elif bmi>=18.5 and bmi<=24.9:
    print("you are Normel, mainten your body")
elif bmi>=30.0 and bmi<=34.9:
    print("you are obese, eat less and walk")
elif bmi>=35.0:
    print("you are Extremely obese, you need to through and surgery")
else:
    print("you are underweight, you should focus on weight gain")