#built in data types
# str , int, float , complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType
x = 5
print(type(x))
#float
y = 5.4
print(type(y))
#complex
z = 3 + 5j
print(type(z))
#list
a = ['q','e','w']
print(type(a))
#tuple
b = ('f','g','h','i')
print(type(b))
#range
c = range(4)
print(range(4))
#dict
d = {'name':'me', 'age':22}
print(type(d))
#set
e = {1,2,3,4,2,3,4}
print(e)
print(type(e))
#frozenset
#it is immutable version of set
f = frozenset({5,6,7,8,5,6})
print(f)
#bool
g = True
print(type(g))
#bytes
x = b"hello"
print(x)
print(type(x))
#bytearray
y = bytearray(5)
print(y)
import random
print(random.randrange(1,100))
#casting
g = int(3.2)