import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [Rock, Paper, Scissor]

User_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissor.\n"))

if User_choice < 0 or User_choice >= len(game_images):
    print("You typed an invalid number, You lose!")
else:
    print(game_images[User_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if User_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and User_choice == 2:
        print("You lose!")
    elif computer_choice > User_choice:
        print("You lose!")
    elif User_choice > computer_choice:
        print("You win!")
    elif computer_choice == User_choice:
        print("It's a draw.")