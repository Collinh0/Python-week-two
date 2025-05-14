"""
Control Flow -> depends on boolean expressions
->Thye order of execution
->We are able to control the said order
"""
# 1. Conditional Statements
age = 17
if age >= 18:  #the if only checks for truthy
    print("You are an adult")
else: 
    print("You are a minor")

    message = "Ok" if age>20 else "Not ok"\
            "Adult" if age >= 18 else "minor" \
            "teenager" if age >= 13 else "child"\
            "Third floor" if age >= 30 else "Second floor"
    
    score = 67
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 50:
        print("Grade C")
    else:
            print("Grade D")



def grader(score):
     #This checks for falsey
     if score < 0 or score > 100:
          return "Invalid score"
     if score >= 0 and score <=100 :
          #check for truthy
          pass
     else:
            return "Invalid score"

# 2. Loops using for loop
colors = ['red', 'green', 'blue', 'yellow', 'mlue']
for color in colors:
    print(color)

    #range -. inbuilt fn that generates a sequence of numbers
for i in range(5):
    print(i) # prints 0, 1, 2, 3, 4
    

# 3. While Loops execute blocks of codes repeatedly as long as the given condition is true.
count = 0
while count < 5