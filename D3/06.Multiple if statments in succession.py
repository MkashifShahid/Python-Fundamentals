print("Welcome to The Roller Coaster 2.0!")
height=float(input("Please Enter Your Height in cm:"))
bill=0
if height >= 120:
    print("You can ride the Roller coaster!")
    age=float(input("Please Enter Age :"))
    if age <12:
        bill=5
        print(f"Child Ticket are {bill}$.")
    elif age <=18:
        bill=7
        print(f"Youth tickets are {bill}$. ")
    else:
        bill=12
        print(f"Adult tickets are {12}$.")
    want_photo=input("Do you want a photo Taken? Y or N :")
    if want_photo=="Y" or want_photo=="y":
        
        # bill=bill+3
        bill+=3   
        print(f"Your final Bill is {bill}$ ")
    else:
        print(f"Your Final Bill {bill}$.")
else:
    print("Sorry, you have to grow taller before you can ride.")

    