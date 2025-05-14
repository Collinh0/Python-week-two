"""
Decorators -> design pattern that allows us to modify the functionality of a fn wi9thout necessarily modifying the fn code itself.
-It uses the @ symbol on functions

"""

#how to create a decorator
def logger(func):
    #define another inner function
    def inner():
        print("decorator is running before fn")
        #execfute the original fn
        func()

 #return inner

@logger
def check_mic():
    print("id the mic working?")



check_mic()

decorated_func = logger(check_mic)

#call execute the inner fn
decorated_func()

def modifier(func):
    def inner(a, b):
        #modify argument a
        a = a + 5
        #call the original function
        func (a, b)
        return func(a + b)
    return inner

def validator(func):
    def inner(a, b):
        #check if the args are type int
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            print("Args must be type int")
    return inner

@modifier
def calculate(a, b):
    print(a + b)
    return a + b

@validator
def multiply(x, y):
    print(x * y)
    return x * y

print(calculate(3, 3))
print(calculate("WED", "Thur"))


        