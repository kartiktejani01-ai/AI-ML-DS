# write a program to print day and night choghadiya of given day of week.
days = int(input("Enter Day of Week (1 to 7)"))

match days:
    case 1:
        print("""Monday
        Day: Amrit, Kaal, Shubh, Rog, Udveg, Chal, Labh, Amrit
        Night: Chal, Rog, Kaal, Labh, Udveg, Shubh, Amrit, Chal""")

    case 2:
        print("""Tuesday
        Day: Rog, Udveg, Chal, Labh, Amrit, Kaal, Shubh, Rog
        Night: Kaal, Labh, Udveg, Shubh, Amrit, Chal, Rog, Kaal""")
    case 3:
        print("""Wednesday
             Day: Labh, Amrit, Kaal, Shubh, Rog, Udveg, Chal, Labh
            Night: Udveg, Shubh, Amrit, Chal, Rog, Kaal, Labh, Udveg""")
    case 4:
        print("""Thursday
            Day: Shubh, Rog, Udveg, Chal, Labh, Amrit, Kaal, Shubh
            Night: Amrit, Chal, Rog, Kaal, Labh, Udveg, Shubh, Amrit""")
    case 5:
         print("""Friday
            Day: Chal, Labh, Amrit, Kaal, Shubh, Rog, Udveg, Chal
            Night: Rog, Kaal, Labh, Udveg, Shubh, Amrit, Chal, Rog""")
    case 6:
         print("""Saturday
            Day: Kaal, Shubh, Rog, Udveg, Chal, Labh, Amrit, Kaal
            Night: Labh, Udveg, Shubh, Amrit, Chal, Rog, Kaal, Labh""")
    case 7:
         print("""Sunday
            Day: Udveg, Chal, Labh, Amrit, Kaal, Shubh, Rog, Udveg
            Night: Shubh, Amrit, Chal, Rog, Kaal, Labh, Udveg, Shubh""")
    case _:
        print("This is not valid Day for Week")