#1-Simple Math Operations 
print(8/3) 

#2-Round Function  
print(round(8/3,2))  # Round to 2 decimal places
print(round(2.6666666666666666666666,3)) # Round to 3 decimal places

#3-Floor Devision [ instead of Round ]
print(8//3)  # 2.6666666666666665 -> 2
print(8//3.0)  # 2.6666666666666665 -> 2.0

#4-If we save the result of 8/3 in a variable and again devide it with another number
#   Result ?
Result=8/3
print(Result)
Result/=2
print(round(Result,2))  #It Take 2 numbers after floating point due to Round function.

#5-Short Hand Notation
Score=0
Score+=1
print(Score) # 1
marks=10
marks-=1
print(marks) # 9

#6-F-Strings
Score=10 # Integer
hight=1.8 # Float
isWinning=True # Boolean
# print("Your score are :"+ Score) # TypeError: can only concatenate str (not "int") to str
# If want to print the score with string then we have to convert the integer into string
print("Your score are : "+ str(Score)) # Your score are : 10

# But if we use F-Strings  ????????
print(f"Your score are : {Score}, Your height is : {hight}, Your Winning status is : {isWinning}") # Your score are : 10, Your height is : 1.8, Your Winning status is : True
