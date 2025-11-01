x="Pakistan is a {} country and its capital is {}".format("great","Islamabad")
print(x)
x="Pakistan is a {1} country and its capital is {0}".format("great","Islamabad")
print(x)
x="Pakistan is a {0} country and its capital is {1}".format("great","Islamabad")
print(x)
x="Pakistan is a {1} country and its capital is {1}".format("great","Islamabad")
print(x)

#Lenght Fun
city="Lahore"
print("The Lenght of a ",city,"is",len(city))

#Min and Max fun( works on ASCII)
city="Alipuraliwala"
#A= 65, B=66 .... and a=97  ----> To iss Hisaab sy hamary code min A ke ASCII value kum hai owr A he print ho ga 
y=min(city)
print(y)
z=max(city)
print(z)

#sort fun ----> it also works on ASCII--->have less less Value comes First.
g=sorted(city) 
print(g)
x=sorted(city,reverse=True)
print(x)

#Upper , lower and Captalize fun
print("LAHORE".lower())
print("lahore".upper())
print("lHORE cITY".capitalize())