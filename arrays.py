#arrays in python are referred to lists

cars = ["BMW","Volvo","Benz"]


x = cars[0]
print(x) #print the first car element in the array

 #adding element into the array
cars.append("Tx")
print(cars) #printing the array

z = len(cars)
print(z)

#for in loop in array
#poping an element from an array
cars.pop(1)

for i in cars:
    print(i)

