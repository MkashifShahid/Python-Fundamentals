#sol :01
total=0
for Number in range (2,101,2):
    total+=Number
print(f"The Sum of Even Numbers is {total}")

#sol :02
total1=0
for number in range (1,101):
    if number%2==0:
        total1+=number
print(f"The sum of Even Numbers is {total1}")