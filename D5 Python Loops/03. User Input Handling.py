student_score = input("Input a list of Student scores, separated by spaces: ").split()
# Convert the list of score strings to a list of integers
for n in range(len(student_score)):
    student_score[n] = int(student_score[n])

print("The highest score is:", max(student_score))
print("The lowest score is:", min(student_score))
