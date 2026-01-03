#operators are used to perform operations on variables and values
#1 Arithmetic operators
a = 10
b = 20
#addition
print(a+b)
#subtraction
print(b-a)
#multiplication
print(a*b)
#division
print(b/a)
#modulus
print(b%a)
#exponentiation
print(a**3)
#floor division
print(b//a)
#2 ASSIGNMENT OPERATORS
x = 5
x += 10 # x = x+10
print(x)
x -= 10 #x = x -10
print(x)
x *= 2 #x = x*2
print(x)
x /= 5 #x = x/5
print(x)
x %= 5
print(x)
x **= 3
print(x)
x //= 2
print(x)
#3 comparision operators
# equals to ==
#less than <
#greater than >
#less than or equal to <=
#greater than or equal to >=
#not equal to !=
#logical operators
#and or not
#4 LOGICAL OPERATORS
#and , or , not
x = 10
print(x>5 and x <11)
print(x>5 or x<9)
print(not(x>5 and x<9))
#5 IDENTITY OPERATORS
#is , is not
a = 5
b =5
print(a is b)
print(a is not b)
x = [1,2,3]
y = [1,2,3]
print(x is y)
print(x is not y)
#6 MEMBERSHIP OPERATORS
#in , not in
fruits = ['apple', 'banana', 'mango']
print("apple" in fruits)
print('custard' not in fruits)
#BITWISE OPERATORS
#and , or, not, xor, left shift, right shift
print(6&3) #and
print(6|3) #or
print(~6) #not
print(6^3) #xor
print(6<<2) #left shift
print(6>>2) #right shift
#7 SPECIAL OPERATORS
#Ternary Operator
a = 10
b = 20
max = a if a>b else b
print(max)
#Walrus Operator
n = 10
if (m := n + 5) > 12:
    print(m)
#Lambda Operator
square = lambda x: x*x
print(square(5))
#Generator Expression
squares = (x*x for x in range(5))
for square in squares:
    print(square)
#List Comprehension
cubes = [x*x*x for x in range(5)]
print(cubes)
#Dictionary Comprehension
squared_dict = {x: x*x for x in range(5)}
print(squared_dict)
#Set Comprehension
squared_set = {x*x for x in range(5)}
print(squared_set)
#Augmented Assignment Operators
x = 5
x += 3
print(x)
x *= 2
print(x)
x -= 4
print(x)
