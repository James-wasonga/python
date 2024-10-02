thistuple = ("Maseno","Kenyatta","UoN","MKU")
print(thistuple)

# accessing a specific item in a tuple
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

fruittuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruittuple[-4:-1])
if "apple" in fruittuple:
    print("apple is in the fruit list")
else:
    print("apple does not exist in the fruit list")
    
    
# updating item on the tuple is by converting the tuple to list, update the list then convert the list back to the tuple
thistuple =  ("apple","banana","cherry")
mylist = list(thistuple)
mylist[0] = "orange"
thistuple = tuple(mylist)
print(thistuple)

# add item to the tuple
thistuple =  ("apple","banana","cherry")
mylist = list(thistuple)
mylist.append("melon")
thistuple = tuple(mylist)
print(thistuple)

# remove item from the tuple
thistuple =  ("apple","banana","cherry")
mylist = list(thistuple)
mylist.remove("cherry")
thistuple = tuple(mylist)
print(thistuple)