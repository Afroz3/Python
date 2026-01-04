set = {'apple','banana','mango','orange'}
#sets are unordered
#duplicates are not allowed
#ACCESSING SET THINGS
#you cannot access items in a set by referring to an index
#you can loop through set items using for loop and while loop and in keyword
for x in set:
    print(x)
#ADDING ITEMS TO SET
set.add('watermelon')
set.add('grapes')
print(set)
#adding sets to sets
set2 = {'kiwi', 'pineapple', 'custard'}
set.update(set2)
print(set)
#remove items from set
set.remove('banana')
print(set)
#loop through set items
for x in set:
    print(x)
#joining sets
#union method
set3 = set.union(set2)
print(set3)
set3 = set | set2
print(set3)
#frozen set
#it is an immutable version of set
#it has no add or remov methods
fset = frozenset({'a','b','c','d'})
print(fset)
#methods
#add()
#clear()
#copy()
#difference()
#difference_update()
#discard()
#intersection()
#intersection_update()
#isdisjoint()
#issubset()
#issuperset()
#pop()
#remove()
#symmetric_difference()
#symmetric_difference_update()
#union()
#update()
