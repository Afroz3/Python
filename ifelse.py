#python supports the usual logical conditions from mathematics:
#equals: a == b
#not equals: a != b
#less than: a<b
#less than or equal to: a <= b
#greater than: a>b
#greater than or equal to: a >= b
#these conditions can be used in several ways, most commonly in "if statements" and loops
a =33
b = 200
if b>a:
    print('b is greater than a')
else:
    print(' a is greater than b')
number = 15
if number < 10:
    print('number is less than 10')
else:
    print('number is greater than or equal to 10')
#program to check if a person is eligible to vote
'''age = int(input('enter you age :'))
if age >= 18:
    print('you are eligible')
else:
    print('NA')'''
#program to check if a number is even or odd
'''n = int(input('enter a number :'))
if n % 2 == 0:
    print('even')
else:
    print('Odd')'''
#program to check if a number is divisible by 7
'''n = int(input('enter a number :'))
if n % 7 == 0:
    print('divisible')
else:
    print('not divisible')
n = int(input('enter a number :'))
if n % 5 == 0:
    print('Hello')
else:
    print('Bye')'''
#program to calculate the electricity bill
'''amt = 0
units = input('enter your units :')
if units <= 100:
    amt = 0
elif units > 100 and units <= 200:
    amt = (units-100)*5
else:
    amt = 500+(units-200)*10
print(amt)'''
'''n = int(input('enter a number :'))
lastnum = 0
if n >= 10:
    lastnum = n % 10
else:
    lastnum = 'invalid'
print('last num is',lastnum)'''
l = [1,2,3,4,5,True]
l.pop(True)
print(l)
#pass statement
#if statement cannot be empty, but if you for some reason have if condition without content put the pass statement to avoid
a = 33
b = 44
if b > a:
    pass
