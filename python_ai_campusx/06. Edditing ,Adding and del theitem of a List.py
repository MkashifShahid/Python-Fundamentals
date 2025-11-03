l=[1,2,3,4,5,4.5, "Mks","ALi"]
l[0]=1000
l[1:4]=[10,20,30] #First included last Excluded
print(l)

#Addition 
l.append("jaffar")
print(l)
l.extend(["ali","Hassan","fad"])
print(l)
l.insert(1,"Lahore")
print(l)

#Deletion
del l[0]
print(l)

#Remove
l.remove("Lahore")
print(l)

#POP---->Del only last item
l.pop()
print(l)

#clear ---->clear the whole list(not del the list)
l.clear()
print(l)