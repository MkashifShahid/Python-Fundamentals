''' 
Congratulations, you've got a job at Python Pizza. Your first job is to build 
an automatic pizza order program.
Based on a user's order, work out their final bill:
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium and Large Pizza: +$3 and +$4
Extra cheese for any size pizza: +$1
Let me know if you need help coding this! '''

print("welcome to python Pizza Deliveries!:")
size=input("What size do you want ? S , M,L:")
add_pepperoni=input("Do you want Pepperoni ? S,M,L:")
Extra_cheese=input("Do You want Extra Cheese? Y ,N :")

bill=0

if size=='S' or size=='s':
    bill+=15
elif size=='M' or size=='m':
    bill+=20
elif size =='L' or size=='l':
    bill+=25
else:
    print("Invalid size option. Please restart your order.")
if add_pepperoni== 's' or add_pepperoni=='S':
    bill+=2
elif add_pepperoni=='M' or add_pepperoni=='m':
    bill+=3
else:
    bill+=4
    
if Extra_cheese =='Y' or Extra_cheese=='y':
    bill+=1
    print(f"Thank you for your order! Your final bill is +${bill}.")
    
elif Extra_cheese=='N' or Extra_cheese=='n':
    print(f"Thank you for your order! Your final bill is +${bill}.")
    
else:
    print("Invalid input for extra cheese. Please restart your order! ")
    