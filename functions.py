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
'''def my_function(x,y):
    return x+y
result=my_function(5,5)
print(result)'''
#returning different data types
'''def my_function():
    return ['apple', 'banana', 'cherry']
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])'''
'''def my_function():
    return (10, 20)
x, y = my_function()
print('x:', x)
print('y:', y)'''
#positional only arguments
'''def my_function(name,/):
    print('hello',name)
my_function('john')'''
#keyword only arguments
#to specify that a function can have only keyword arguments, add*, before the arguments
#combining positional only and keyword only
'''def my_function(a,b,/,*,c,d):
    return a+b+c+d'''
'''result = my_function(10,5,c=15,d=20)
print(result)'''
#python *args and **kwargs
#by default a function must be called with the correct number of arguments
#however sometimes you may not know how many arguments that will be passed into your function
'''def my_function(*kids):
    print('the youngest kid is ' + kids[2])
my_function('emil','tobias','john')'''
#what are *args
#the *args parameter allows a function to accept  any number of positional arguments
def my_function(*args):
    print('Type:', type(args))
    print('first arguments: ',args[0])
    print('second arguments', args[1])
    print('all arguments',args)
my_function('emil','sara','john')
#use *args with  regular arguments
#you can combine regular parameter with *args
#regular parameters must come before *args
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1,2,3))