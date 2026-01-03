#used to store multiple items in a single variable
#it is immutable
#tuples are created using paranthesis ()
tuple = ('apple', 'banana', 'cherry', 'orange')
#they also allow duplicates
#ACCESSING TUPLES
#they also have indexing and slicing same as lists and same functions to access items
#change tuple values
#you can change the tuple to list then add pop make any function and convert it back to tuple
#unpack tuples
#in tuple unpacking the values are assigned to multiple variables in a single statement
green, yellow, red, black = tuple
print(green)
print(yellow)
print(red)
print(black)
#asterisk * can be used to assign the remaining values to a variable
green, yellow, *red = tuple
print(green)
print(yellow)
print(red)
#loop through a tuple
for x in tuple:
    print(x)
#join tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)
#multiply tuples
tuple4 = tuple3 * 2
print(tuple4)
#tuple methods
#count() method returns the number of times a specified value occurs in a tuple
print(tuple4.count('a'))
#index() method searches the tuple for a specified value and returns the position of where it was found
print(tuple4.index(2))
