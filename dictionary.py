dicti = {
    'car':'bmw',
    'model':'m4',
    'year': 2026
}
'''print(dict)
#duplicates are not allowed
#we can access items by referring to its key name
print(dict['model'])
print(len(dicti))'''
'''set = dict(car = 'audi', model = 'r8', year = 2018)
print(set)'''
#accessing items
'''x = dict.get('car')
print(x)
y = dict.keys()
print(y)
y = dict.values()
print(y)
x = dict.items()
print(x)'''
'''car['color'] = 'red'
print(dict)'''
#changing items
'''dict['year'] = 2027
print(dict)
dict.update({'model':'m5'})
print(dict)
#adding items
dict.update({'color':'black'})
print(dict)
#removing items
#pop #popitem #del #clear'''
'''dict.pop('model')
print(dict)
dict.popitem()
print(dict)
del dict['year']
print(dict)
dict.clear()
print(dict)'''
#loop dictionaries
'''for x in dict:
    print(x)
for x in dict:
    print(dict[x])
for x in dict.values():
    print(x)
for x, y in dict.items():
    print(x,y)
#copy dictionary
dict1 = dict.copy()
print(dict1)'''
dict2 = dict(dicti)
print(dict2)
#nested dictionary
myfamily = {
    "child1":{
        'name':'me',
        'year':2003
    },
    'child2':{
        'name':'you',
        'year': 2004
    },
    'child3':{
        'name':'him',
        'year': 2005
    }
}
class1:{
    'student1':'john',
    'age': 20
}
class2:{
    'student2':'anna',
    'age':22
}
class3:{
    'student3':'peter',
    'age':21
}
myclass = {
    'class1' : 'student1',
    'class2' : 'student2',
    'class3' : 'student3'
    }
print(myclass)
print(myfamily)
print(myclass['class2'])
print(myfamily['child1']['name'])
#dictionary methods
