'''Write a program to determine whether a given year is a leap year. A regular year has 365 days, while a leap year has 366 days, including an extra day in February. The concept of leap years is very interesting; this video explains it in detail for Urdu speakers:
https://youtu.be/4w18EFuwPSA?si=vTAM2Ora0q_hFyx3'''

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
