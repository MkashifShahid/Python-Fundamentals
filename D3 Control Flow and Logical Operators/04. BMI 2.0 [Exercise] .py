"""
Write a Python program to calculate and interpret the Body Mass Index (BMI) 
based on user input.

The program should classify the BMI into the following categories:

- BMI < 18.5: Underweight
- 18.5 <= BMI < 25: Normal weight
- 25 <= BMI < 30: Overweight
- 30 <= BMI < 35: Obese
- BMI >= 35: Clinically obese
"""

Weight=float(input("Please Enter Your Weight in KG:"))
height=float(input("Please Enter Your Height IN cm:"))

BMI= round(Weight/(height**2))
if BMI <18.5:
    print(f"Your BMI is {BMI},Your are Underweight")
elif BMI<25:
    print(f"Your BMI is {BMI}, You have a normal weight")
elif BMI<30:
    print(f"Your BMI is {BMI}, Overweight")
elif BMI<35:
    print(f"Your BMI is {BMI}, Obese ")
else:
    print(f"Your BMI is {BMI},Your Clinically Obese ")

