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
#polymorphism means having many forms
#it refers to methods/functions/operators with the same name that can be executed on many objects or classes
#class polymorphism
'''class car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def move(self):
        print('Drive')
class ship:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def move(self):
        print('Sail')
class plane:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def move(self):
        print('Fly')
car1 = car('ford','mustand')
ship1 = ship('credilia','titanic')
plane1 = plane('airbus','a120')
for x in (car1,ship1,plane1):
    x.move()
print(car1.brand,car1.name)'''
#encapsulation
#encapsulation is about protecting data inside a class
#it means keeping data and methods together in a class while controlling how the data can be accessed from outside the class
#this prevents accidental modification of data and hides the internal details of how the class works
#private properties
'''class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
p1 = person('john',36)
print(p1.name)
print(p1.get_age())'''
#set private property value
#to modify a private property you can create a setter method
# setter method can also validate before setting the value
'''class person:
    def __init__(self,name,age):
        self.name= name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print('age must be positive')
p1 = person('john',36)
print(p1.get_age())'''
#why to use encapsulation
#data protection : prevents accidental modification of data
#validation : allows validation before setting values
#flexibility : internal implementation can be changed without affecting external code
#control : you have full control how data is accessed and modified
'''class student:
    def __init__(self,name):
        self.name = name
        self.__grade = 0
    def set_grade(self,grade):
        if grade >= 0 and grade <= 100:
            self.__grade = grade
        else:
            print('enter valid grade')
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade >=40:
            return 'pass'
        else:
            return 'fail'
s1 = student('john')
s1.set_grade(31)
print(s1.get_grade())
print(s1.get_status())'''
#protected properties
'''class person:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
p1 = person('john',1000)
print(p1.name)
print(p1._salary)'''#can access but shouldn't be accessed directly
#inner class
#an inner class is defined inside another class
#the inner class can access the properties and methods of the outer class
#inner classes are useful for grouping classes that are used only in one place making your code more organized
#example of inner class
'''class outer:
    def __init__(self):
        self.name = 'outer class'
    class inner:
        def __init__(self):
            self.name = 'inner class'
        def display(self):
            print('this is inner class')
Outer = outer()
Inner = outer.inner()
print(Outer.name)
print(Inner.name)'''
#accessing inner class from the outside
'''class outer:
    def __init__(self):
        self.name = 'outer class'
    class inner:
        def __init__(self):
            self.name = 'inner class'
        def display(self):
            print('this is inner class')
Outer = outer()
Inner = outer.inner()
Inner.display()'''
#accessing outer class from inner class
'''class Outer:
    def __init__(self):
        self.name = 'john'
    class Inner:
        def __init__(self,outer):
            self.outer = outer
        def display(self):
            print(f'outer class name is {self.outer.name}')
outer = Outer()
inner = outer.Inner(outer)
inner.display()'''
'''class Car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
        self.engine = self.Engine()

        class Engine:
            def __init__(self):
                self.status = 'off'
            def start(self):
                self.status = 'Running'
                print('engine started')
            def stop(self):
                self.status = 'off'
                print('engine stopped')
            def drive(self):
                if self.status == 'Running':
                    print(f'driving the {self.brand} {self.model}')
                else:
                    print('start the engine first')
car1 = Car('tata','safari')
car1.drive()
car1.engine.start()
car1.drive()'''
#many inner classes
'''class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()
    class CPU:
        def process(self):
            print('processing data')
    class RAM:
        def store(self):
            print('storing data')
computer = Computer()
computer.cpu.process()
computer.ram.store()'''
