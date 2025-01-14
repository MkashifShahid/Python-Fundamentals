print("Welcome to the Roller Coaster!")
height=int(input("Please Enter Your Height in cm:"))
if height >= 120:
    print("You can Ride The Roller Coaster!")
    age=int(input("please Enter Your age:"))
    if age <=5:
        print("Its Free For You. (100% Discount)")
    elif age <=12:
       print("Please Pay 5$")
    elif age <=18:
        print("Please Pay 7$")
    else:
          print("Please Pay 12$")
    
else:
     print("Sorry, you have to grow taller before you can ride.")

        

