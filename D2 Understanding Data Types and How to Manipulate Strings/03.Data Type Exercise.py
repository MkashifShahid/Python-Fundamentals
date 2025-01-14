# Create a program that calculates the sum of the digits in a two-digit number.
# For example, if the input is 35, the output should display 3 + 5 = 8.

# Hint: We will use the concept of subscripting to get the first and second digit.
3
two_digit_number = input("Please Enter a two-digit number: ")  # This will return a string.
first_num = two_digit_number[0]
second_num = two_digit_number[1]
sum = int(first_num) + int(second_num)
print("The sum of the digits in the two-digit number is:", sum)
