num_Char=len(input("Please Enter your name: ")) 
print("The number of characters in your name is", num_Char)
print("The Data type of Your name is ",type(num_Char))

#But We Face an Error when we do cancatenation with a string and an integer
#So we need to convert the integer to a string
#We can do this by using the str() function

#print("The number of characters in your name is: "+num_Char+ "characters") 
#This will give an error

num_char=str(num_Char) #This will convert the integer to a string [Type Conversion or Type Casting]
print("Your name has " +num_char+  "  characters") #This will work

 