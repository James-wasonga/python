import numpy as np

arr = ([1,2,3,4,5,6,7])
filter_arr = []

for element in arr:
    filter_arr.append(True)
else:
    filter_arr.append(False)
    
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)