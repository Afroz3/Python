#creating a variable
x =10
print(x)
#casting
y=str(3)
z=float(6)
print(y)
print(z)
#to get the type of data type
print(type(x))
#string values are given in single or double quotes
name = 'john'
output = "hello"
print(name)
print(output)
#case sensitive
#if you create a variable with a it gives different value than  A
a =4
A = 5
print(a)
print(A)
#assigning multiple values to multiple variables
x,y,z = "Orange", "Custard", "Mango"
print(x)
print(y)
print(z)
#assigning same value to multiple variables
a = b = c = "Agent"
print(a)
print(b)
print(c)
#extracting values from a list or tuple is called unpacking
cars = ["cooper", "ford", "tata"]
c,e,f = cars
print(c)
print(e)
print(f)
#output variables
x ="iam"
y="learning"
z="pyhton"
print(x,y,z)
#global variables
#varaibles which are create outside a function are called global variables
s = "awesome"
def func():
    print("python is", + s)
func()
#to create a global variable inside a function use global keyword
def var():
    global t
    t ='fantastic'
    print('python is ', + t)
var()
print('its' + t)