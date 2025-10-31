email = input("Please Enter your Email: ")
passwd = input("Please Enter Passwd: ")

if "@" in email:
    if email == "admin@gmail.com" and passwd == "1234":
        print("Welcome User")
    elif email == "admin@gmail.com" and passwd != "1234":
        print("Wrong password. Try Again!")
        newpass = input("Please enter your password again: ")
        if newpass == "1234":
            print("Finally Welcome User!")
        else:
            print("Wrong again! Access denied.")
    else:
        print("429: Too many Requests!")  # Aim: without loop
else:
    print("Invalid email or password. Please try again.")
