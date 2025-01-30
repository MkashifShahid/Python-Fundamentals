student_heights = input("Input a list of student heights: ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Initialize total height to 0
total_height = 0

# Calculate the total height by adding each student's height
for height in student_heights:
    total_height += height

# Calculate the average height and round it to the nearest whole number
average_height = round(total_height / len(student_heights))

# Print the average height
print(f"The Average Height is {average_height}")