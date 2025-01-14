import random

# Prompt the user to input names separated by commas
name_string = input("Give me everybody's names, separated by a comma: ")

# Split the input string into a list of names using ',' as the delimiter
names = name_string.split(",")

# Get the length of the list of names
length_of_names = len(names)

# Randomly select an index from 0 to length_of_names - 1
random_choice = random.randint(0, length_of_names - 1)

# Get the name at the randomly selected index
bill_payer = names[random_choice].strip()

# Print the name of the person who will pay the bill
print(f"{bill_payer} will pay the bill today!")