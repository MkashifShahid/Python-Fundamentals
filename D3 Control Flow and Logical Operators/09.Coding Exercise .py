''' A program that tests the compatibility between two people using
a super scientific method recommended by BuzzFeed. To calculate the love score between 
two individuals, you take both people's names and count the number of times the letters
in the word "TRUE" appear. Then, you count the number of times the letters in the word 
"LOVE" appear. Finally, you combine these numbers to form a two-digit number. For more
details, you can refer to this BuzzFeed 
article: https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love.'''

print("Welcome to the Love Calculator.")
name1=input("What is Your name :")
name2=input("what is their name:")

combined_string=name1 +  name2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true= t + r + u + e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love=l+o+v+e

Love_score= int(str(true)+ str(love)) 

if (Love_score < 10) or (Love_score > 90):
    print(f"Your score is {Love_score},You go together like coke and mentos.")
elif (Love_score>=40 ) and (Love_score <=50):
    print(f"Your score is {Love_score},You are alright togather.")
else:
    print(f"The score{Love_score} ")    