# virtual coin toss program. It will randomly tell the user 'Heads' or 'Tails'
import random
random_side=random.randint(0,1)
if random_side==0:
    print("Heads")
else:
    print("Tails")