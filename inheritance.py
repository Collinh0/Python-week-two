#Polymorphism, Encapsulation, Abstraction - (hiding iplementation details)

#Inheritance : it allows a classcalled a child or subclass to inherit attributes and methods from another class called a parent or superclass

#basic syntax
class Parent: #parent class
    def __init__(self):
        pass
    def check(self):
        print("Hello from Parent class")

parent1 = Parent()
parent1.check() # calling the method from the parent class

#child automatically inherit everything from parent
class Child(Parent):
    def __init__(self):
        pass # child class that gets all the attributes from the parent class
    
    def grow_up(self):
        print("Child is growing up")

child = Child()
child.check() 
child.grow_up()

class Person:
    def __init__(self, name,):
        self.name = name
       # self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}")
    
    def walk(self):
        print(f"{self.name} is walking")
    
person1 = Person("Alice")
print("Person",person1.introduce()) 
print("Person",person1.walk())

class Student(Person):
    def __init__(self, name):
        #This allows us to acces parent methods
        #in this case we want the sudent name to be used as the Person name

        super().__init__(name)
        self.name = name
        

student1 = Student("Robert")
print("Student", student1.walk()) 
print("<Student>", student1.introduce())

class Animal:
    def __init__(self, name):
        self.name = name
def eat(self):
    return (f"{self.name} is eating")



crabs = Animal("Crab")
print("<Animal> ->", crabs.name)
print("<Animal> ->", crabs.eat())

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name)
        self.name = name
        self.age = age
        self.breed = breed


#by redifining the methods inthe oarent class, we can be abble to override them (polymorphism)
    def eat(self):
        return (f"{self.name} chewing sugercane")

        #returns a printable version of instance
        def __repr__(self):
            return f"Dog({self.name}, {self.age}, {self.breed})"
    
    
dog1 = Dog("Bosco",3, "Mutina")
print("<Dog> ->", dog1.name)
print("<Dog> ->", dog1.eat()) # dog1 inherits the eat method from Animal class
print("<Dog> ->", dog1.breed)
dog1.eat()

class Car:
    def __init__(self,model)
        self.model = model
    
    def drive(self):
        return f"Car model {self.model} is being driven"
    
    def __repr__(self):
        return f"<Car Model:({self.model}>)"
    
car1 = Car("Mercedes")
print(car1)
print("<Car> ->", car1.drive())



class Toyota:
 def __init__(self, model = "Toyota"):
        self.model = model

super().__init__("model") 

#polymorphism
def drive(self, driver):
    return f"Toyota is being moved around by {driver}"

toyota1 = Toyota()
print("<Toyota> ->", toyota1.drive())

toyota2 = Toyota("Toyota Corolla")
print("<Toyota> ->", toyota2.drive("Wantam"))