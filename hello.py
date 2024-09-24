#sigle line comment in python
print("Hello, World")

"""this is a multiline comment in python since it does not read string literals which are not assigned to a a variable
"""
if 5 > 2:
    print("Five is greater than two")
# if 6 < 8:
    print("Six is less than eight") 
    
    
    #variables
    x  = 8
    y = "python is a very nice language"
    
    print(x)
    print(y)
    
    #specifing the data type through casting 
    
    x = str(2)
    y = int(3)
    z = float(3)
    w = 'sodas'
    print(x)
    print(type(w))
    
    #assigning a single value multiple variables
    
    x = y = z = "python guru"
    print(x)
    print(y)
    print(z)
    
    #tuple in python and destructuring of the tuple
     
    fruits = ['Apple','Mango','Orange']
    first, second, third = fruits
    print(first)
    print(second)
    print(third)
    
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)
    
    
    #global variables
    
    x = 'learning python'
    
    def myfunc():
        print("currently I am "+ x)
        
    myfunc()
    
    
    def myGreeting():
        global greet
        greet = "Hello"
    myGreeting()
    
    print(greet + " Everyone")
