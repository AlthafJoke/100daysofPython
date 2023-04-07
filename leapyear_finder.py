print("**Leap year finder**")
year = int(input("Enter the year to find the leap year: "))

print(year / 400)


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")

else:
    print(year, "is not a leap year")




    

