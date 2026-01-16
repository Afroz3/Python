'''#function is block of code which runs when it is called
#function helps code repetition
#creating a function
def func():
    print('hello from a function')
func()
func()
func()'''
#why to use functions
'''def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)* 5/9
print(fahrenheit_to_celsius(96.8))'''
#return values
'''def get_greeting():
    return 'hello'
message=get_greeting()
print(message)'''
'''def greet():
    return 'hello from a function'
print(greet())'''
#pass statement
#Arguments in functions
#information can be passed to functions as arguments
#arguments are specified after the function name inside the parentheses. you can add as many arguments as you want, just separate them with a comma
'''def my_function(fname):
    print(fname + ' refsnes')
my_function('john')'''
#parameters vs arguments
#both pass information to the function
'''def my_function(name):
    print('hello', name)
my_function('john')'''
#number of arguments
'''ef my_function(fname,lname):
    print(fname + " " + lname)
my_function('john','jin')
'''
#default parameter
#you can assign default parameters if function is called without an argument it uses default values
'''def my_function(name = 'friend'):
    print('hello', name)
my_function('john')'''
'''def my_function(country = 'India'):
    print('Iam from', country)
my_function('Norway')
my_function('Sweden')
my_function()
my_function('germany')'''
#keyword arguments
#you can send arguments with th key = value syntax
'''def my_function(animal,name):
    print('I have a', animal)
    print('My', animal, 'name is', name)
my_function(animal = 'dog', name = 'buddy')'''
#positional arguments
#when you call an arguments without using keywords they are called positional arguments
#they must be in correct order
#mixing positional and keyword arguments
'''def my_function(animal,name,age):
    print('I have an', animal, 'its name is', name, ' and its age is', age)
my_function('dog','emil',4)'''
#passing different data types
#you can send any data type as an argument to a function
#the data type will be preserved inside the function
'''def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ['apple', 'banana', 'cherry']
my_function(my_fruits)'''
'''def my_function(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
my_person = {'name': 'Emil', 'age': 25}
my_function(my_person)'''
#return values
