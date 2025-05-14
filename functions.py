"""
Functions

- Blocks of code that are reusable and can be called multiple times.
- Functions can take inputs (arguments) and return outputs (results).
Modularity -> breaking down complex programs into smaller reusable pieces.
"""

# Function defination
def hello(name): 
    print("Hello {name}, we are learninf about functions") # Function definition

#Calling Function 
hello("Collins")

#1. Positional arguments
def greetings (first_name, last_name):
    print(f"good morning {first_name}, your age is {age}")
#calling the fn
#The order of the arguments matters
greetings(18, "Collins")
greetings("Collins", 18) # This will raise an error because the order of arguments is incorrect

greetings(first_name="Vincent", age=20)
greetings(age=21, first_name="Daud") # This will also work because we are using keyword arguments

# Keyword arguments where arguments are identified by the parameter name which basically make the order irrelevant
greetings(first_name="Collins", age=18)

#we can start with positional arguments and then end with keyword arguments
greetings("Daud", age=23,last_name= "Elmoge")

#kwaegs
greetings(last_name="Haji", first_name="Robert",age=24)

#when starting with positional arguments we have to stick to using them for the remaining args too

greetings(first_name="Irene",age=20)

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

#calling the function
sum(1, 2, 3, 4, 5) # This will return 15
