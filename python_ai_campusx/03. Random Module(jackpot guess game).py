import random
jackpot=random.randint(1,100)
guess=int(input("Guess the number: "))
counter=1
while jackpot!=guess:
    if jackpot>guess:
        print("Guess more high number")
        guess=int(input("Guess the number: "))
        counter=counter+1
    else:
        print("Guess lower number")
        guess=int(input("Guess the number: "))
        counter=counter+1
else:
    print("Congrats,You Won!")
    print("Number of Counter=",counter)