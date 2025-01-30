# Input a list of Student scores, separated by spaces
student_score = input("Input a list of Student scores, separated by spaces: ").split()

# Convert the list of score strings to a list of integers
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

# Initialize the highest score variable
heighest_score = 0

# Calculate the highest score
for score in student_score:
    if score > heighest_score:
        heighest_score = score

# Print the highest score
print(f"The Highest Score in class is: {heighest_score}")