print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[M kashif]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure!")

choice1 = input("You are at a crossroad, where do you want to go? Type 'Left' or 'Right': ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle. Type 'swim' to swim across or 'wait' to wait for a boat: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors. One yellow, one red, and one blue. Which color do you choose? ").lower()
        if choice3 == "yellow":
            print("Congratulations! You won the game 🎉.")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif choice2 == "swim":
        print("You were attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

