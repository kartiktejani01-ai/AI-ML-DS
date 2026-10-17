#write a program to findout whether given number is prime number or not 
number = int(input("Enter Number :"))
deviser = 2

if number%2==0:
    print("It is Prime Number :")
else:
    half = number//2
    while deviser<=half:
            reminder = number%deviser
            if reminder == 0:
                print("It is not Prime Number.")
                break
            deviser = deviser+1
            if deviser>half:
                print("It is Prime Number.")