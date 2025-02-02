# Example of a while loop in Python with additional functionality

# Initialize the counter variable
counter = 0

# Define the condition for the while loop
while counter < 5:
    # Print the current value of the counter
    print(f"Counter is at: {counter}")
    
    # Perform some additional operations
    # Calculate the square of the counter
    square = counter ** 2
    # Print the square of the counter
    print(f"The square of {counter} is {square}")
    
    # Increment the counter by 1
    counter += 1

print("Counter has reached 5, exiting the loop.")