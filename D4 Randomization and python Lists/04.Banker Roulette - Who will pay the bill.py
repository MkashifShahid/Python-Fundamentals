import random

# Get names from the user
name_string = input("Enter names separated by commas: ")

# Split names into a list
names = name_string.split(",")

# Pick a random name
bill_payer = random.choice(names)

# Print the result
print(f"{bill_payer} will pay the bill today!")
