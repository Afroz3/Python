#python iterators
#an iterator is an object that contains countable number of values
tuple = ('apple', 'banana', 'grape')
myit = iter(tuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = 'banana'
it = iter(mystr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for x in tuple:
    print(x)

for x in mystr:
    print(x)
