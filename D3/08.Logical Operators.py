print("Welcome to The Roller Coaster 3.0!")
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
    elif age >18 and age <45:
        bill=12
        print(f"Adult tickets are {12}$.")
    elif age >=45 and age <=50:
        bill=0
        print("Congratulations! You are eligible for a free ride.")
    else:
     print("Invalid option. Please Try again!.")

    want_photo=input("Do you want a photo Taken? Y or N :")
    if age<51 and want_photo=="Y" or want_photo=="y":
        # bill=bill+3
        bill+=3   
        print(f"Your final Bill is {bill}$ ")
else:
    print("Sorry, you have to grow taller before you can ride.")

    