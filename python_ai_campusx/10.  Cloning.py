#Mutibility side effects sy bachny k liya hum cloning ka conecpt use krty hain.

a=[1,2,3,4]
b=a               #Aliasing syntax
print(id(a),id(b))

b.append(5)
print(a,b)  #--->Issue:jub hum b ko change krty hin to a beh chnage ho jata hai .

#Solution/Fix (Cloning)
B=[10,12,13]
C=B[:]
C.append(5)
print(B,C)
print(id(B),id(C))

#Example
T1=(1,2,3,[5,6])
T1[3][1]=1000
print(T1)

a=[1,2]
b=[2,3]
c=(a,b)
print(c,id(a),id(b),id(c))
c[1][0]=1000
print(c,id(a),id(b),id(c))