"""
BMI Calculator

Instructions:
Write a program that calculates the Body Mass Index (BMI) 
from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height.
For example, if a tall person and a short person both weigh the same amount,
the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) 
by the square of their height (in m):
    
    BMI = weight (kg) / height^2 (m^2)

Warning: You should convert the result to a whole number.
"""

# Write your code here
weight=input("Enter Your weight in kg:")
height=input("Enter Your hight in m:")
bmi=int(weight)/float(height)**2
print("Your BMI=",int(bmi)) 