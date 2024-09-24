#dict stores data

thisdict = {
    "brand" : "BMW",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2000
}

print(thisdict["year"])
print(len(thisdict))
print(type(thisdict))

#creating dictionary based on a constructor 

thisdict = dict(name = "James",age = 20, country = "Norway")
print(thisdict)


# creating a dict using a costructor
# dict()

myfruit = dict(name = "mango", place = "Kisumu", number = 30 )
print(myfruit["name"])

myfruit["color"] = "pink"
myfruit["taste"] = "perfect" 
print(myfruit)

myfruit.pop("taste")
del myfruit["color"]
print(myfruit)


# a copy can't be made by "dict2 = dict1 " since the second dict will be a referrenced to the first
# so incase of change of dict1 the second one also changes so there is no copy but a reference to the other 

myfruit2 = myfruit.copy()
print(myfruit2)

