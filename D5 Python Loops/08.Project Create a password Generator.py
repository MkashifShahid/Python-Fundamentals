import random

# Lists of possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '@', '^', '_', '{', '}', '[', ']', '|', ':', ';', '<', '>', '?', '/', '~', 
           '¨', '¬', '¦', '§', '£', '¢', '¥', '©', '®', '±', 'µ', '½', '¿', '×', '÷']

print("Welcome to the password Generator!")

# Get the number of each type of character for the password
nr_letter = int(input("How many letters would you like in your password?\n"))  # Convert input to integer
nr_symbol = int(input("How many symbols would you like?\n"))  # Convert input to integer
nr_number = int(input("How many numbers would you like?\n"))  # Convert input to integer

# Initialize the password list
password = []

# Add random letters to the password list
for char in range(1, nr_letter + 1):
    password.append(random.choice(letters))

# Add random symbols to the password list
for char in range(1, nr_symbol + 1):
    password.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(1, nr_number):
    password.append(random.choice(numbers))

# Shuffle the password list to ensure randomness
random.shuffle(password)

# Join the list elements to form the final password string
New_password = ""
for n in password:
    New_password += n

# Print the final password
print(f"Your password is: {New_password}")