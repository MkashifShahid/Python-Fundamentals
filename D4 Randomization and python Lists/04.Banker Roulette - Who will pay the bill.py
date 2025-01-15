import random

# Prompt the user for names separated by commas
name = input("Please enter names separated with a comma: ")

# Split the names into a list
split = name.split(",")

# Generate a random index
random_index = random.randint(0, len(split) - 1)

# Get the person at the random index
bill_payer = split[random_index]

# Print the result
print(f"{bill_payer} will pay the bill!")
