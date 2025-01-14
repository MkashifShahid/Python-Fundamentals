#01-List
Provinces_of_Pakistan=["Balochistan","Punjab","Sindh","KPK"]
Two_administrative_regions=["Azad Jammu and Kashmir","Gilgit-Baltistan"]
print(f"Pakistan has four provinces {Provinces_of_Pakistan}, two administrative regions {Two_administrative_regions}, and a capital territory.")

#02-Indexing
print(Provinces_of_Pakistan[0])
print(Provinces_of_Pakistan[1])
print(Provinces_of_Pakistan[-1])

#03-Append [Add an item to the end of the list]
Provinces_of_Pakistan.append("DGK")
print(Provinces_of_Pakistan)

#04-Extend [Extend the list by appending all items from the iterable.]
Provinces_of_Pakistan.extend(["Lahore","Karachi","Alipur"])
print(Provinces_of_Pakistan)

#
'''Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''