''' 
write a program to accept birth day and birth month from user as separate input. decide zodiac sign as sun rashi from below table 
    input : day 22 month = 4
    Aries: April 14 – May 14
    Taurus: May 15 – June 14
    Gemini: June 15 – July 16
    Cancer: July 17 – August 16
    Leo: August 17 – September 16
    Virgo: September 17 – October 16
    Libra: October 17 – November 15
    Scorpio: November 16 – December 15
    Sagittarius: December 16 – January 13
    Capricorn: January 14 – February 12
    Aquarius: February 13 – March 13
    Pisces: March 14 – April 13
    '''

day = int(input("Enter your Birth Date :"))
month = int(input("Enter your Birth Month :"))

#days of month in day
days_in_month = [31,29,31,30,31,30,31,30,31,30,31,30]

if month < 1  or month >12 or day < 1 or day > days_in_month[month-1]:
    print("Enter Valid Date & Month")
else:
    #Aries: April 14 – May 14
    if (month == 4 and  day >= 14) or (month == 5 and day <= 14):
        print("Aries")
    #Taurus: May 15 – June 14
    elif (month == 5 and day >= 15) or (month == 6 and day <= 14):
         print("Taurus")
    #Gemini: June 15 – July 16
    elif (month == 6 and day >= 15) or (month == 7 and day <= 16):
        print("Gemini")
    #Cancer: July 17 – August 16
    elif (month == 7 and day >= 17) or (month == 8 and day <= 16):
        print("Cancer")
    #Leo: August 17 – September 16
    elif (month == 8 and day >= 17) or (month == 9 and day <= 16):
       print("Leo")
    #Virgo: September 17 – October 16
    elif(month == 9 and day >= 17) or (month == 10 and day <= 16):
       print("Virgo")
    #Libra: October 17 – November 15
    elif(month == 10 and day >= 17) or (month == 11 and day <= 15):
        print("Libra")
    #Scorpio: November 16 – December 15
    elif(month == 11 and day >= 16) or (month == 12 and day <= 15):
        print("Scorpio")
    #Sagittarius: December 16 – January 13
    elif(month == 12 and day >= 16) or (month == 1 and day <= 13):
        print("Sagittarius")
    #Capricorn: January 14 – February 12
    elif(month == 1 and day >= 14) or (month == 2 and day <= 12):
        print("Capricorn")
    #Aquarius: February 13 – March 13
    elif(month == 2 and day >= 13) or (month == 3 and day <= 13):
       print("Aquarius")
    #Pisces: March 14 – April 13
    else:
        print("Pisces")
