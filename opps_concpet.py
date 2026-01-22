#oops stands for object oriented programming system
#python is object oriented programming language allows you to structure your code using classes and objects for better organization and reusability
#advantages of oops
#provides a clear structure to programs
#makes code easier to maintain,reuse and debug
#helps to keep your code DRY(dont repeat yourself)
#allows you to build reusable applications with less code
#class and object
#classes and objects are the two core concepts in oops
#class defines what an object should look like and what t should do
#almost everything in python is an object with its properties and methods
#a class is like an object constructor or a blueprint for creating objects
#creating a class
'''class Myclass:
    x = 5'''
#creating an object
'''p1 = Myclass()
print(p1.x)'''
#deleting object
'''del p1
'''#multiple objects
'''p1 = Myclass()
p2 = Myclass()
p3 = Myclass()
print(p1.x)
print(p2.x)
print(p3.x)'''
#pass statement
'''class Person:
    pass'''
#init method
#all classed have a built in method called __init__() which is always executed when the class is being initiated
'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("John",36)
print(p1.name)
print(p1.age)'''
'''class Person:
    def __init__(self,car,model,year):
        self.car = car
        self.model = model
        self.year = year
p1 = Person('ford','mustang',2026)
print(p1.car)
print(p1.model)'''
'''class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
p1 = Person('alice')
print(p1.name)
print(p1.age)'''
#SELF PARAMETER
#self parameter is a reference to the current instance of the class
#it is used to access properties and methods to the class
'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print('hello my name is' +self.name +'and my age is ' + str(self.age))
p1 = Person('john',21)
p1.greet()'''
'''class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def description(self):
        print(f'{self.year} {self.brand} {self.model}')
car1 = Car('toyota','fortuner',2026)
car1.description()'''
#calling methods with self
'''class person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        return 'hello my name is ' + self.name
    def welcome(self):
        message = self.greet()
        print(message + ' welcome to the community!')
p1 = person("john")
p1.welcome()'''
#python class properties
'''class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person('john',36)
print(p1.name)
print(p1.age)
p1.age = 40
print(p1.age)'''
#inheritance
#allows you to define a class that inherits all the methods and properties from another class
#parent class is the class being inherited from also called base class
#Child class is the class that inherits from another class also called derived class
'''class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname , self.lname)
p1 = person('john','doe')
p1.printname()
#create a child class
class Student(person):
    pass
x = Student('mike','smith')
x.printname()
#add the __init__() function to the child class
class Student(person):
    def __init__(self,fname,lname):
#super() function allows you to call the __init__() method of the parent class
        super().__init__(fname,lname)
        x = Student('mike','smith')
        x.printname()
'''
#polymorphism
