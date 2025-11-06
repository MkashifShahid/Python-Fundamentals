dic={"Name":"kashif","age":21,"city":"Lahore"}
print(dic)
type=type(dic)
print(type)
print(dic["Name"])
print(dic["age"])
dic["Name"]="Muhammad kashif shahid"
print("Updated Dic is=",dic)
dic["Nationality"]="Pakistan"
print(dic)
del dic["age"]
print(dic)
B="city" in dic  #Membership Operator
print(B)

for i in dic:
    print(i,"=",dic[i])