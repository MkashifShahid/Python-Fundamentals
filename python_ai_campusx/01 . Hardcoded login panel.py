email = input("Please Enter your Email: ")
if "@" in email:
    passwd = input("Please Enter Passwd: ")
    if email == "admin@gmail.com" and passwd == "1234":
        print("Welcome User")
    elif email == "admin@gmail.com" and passwd != "1234":
        print("Wrong password. Try Again!")
        newpass = input("Please enter your password again: ")
        if newpass == "1234":
            print("Finally Welcome User!")
        else:
            print("429: Too many Requests!")
    else:
        print("Access denied.")  # Aim: without loop
else:
    print("Invalid email!")
