dict = {
    'car':'bmw',
    'model':'m4',
    'year': 2026
}
print(dict)
#duplicates are not allowed
#we can access items by referring to its key name
print(dict['model'])
print(len(dict))
'''set = dict(car = 'audi', model = 'r8', year = 2018)
print(set)'''
#accessing items
x = dict.get('car')
print(x)
y = dict.keys()
print(y)
y = dict.values()
print(y)

