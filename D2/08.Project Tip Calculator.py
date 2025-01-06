print("Welcome to the Tip Culculator")
bill=float(input("what was the total bill?$ "))
Tip=int(input("What perncentage tip would you like to give 10, 12, or 15? "))
People=int(input("How many people to split the bill? "))
bill_with_tip=Tip/100*bill+bill
bill_per_person=bill_with_tip/People
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")    
print("Total bill with tip: $",bill_with_tip)
print("Thank you for using the Tip Calculator")