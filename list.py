#lists are used to store multiple items in a single variable
#created using square brackets []
#list items are ordered, changeable, and allow duplicate values
#1 creating a list
mylist = [1,2,3,'humm',4.5]
print(mylist)
#list is changeable, meaning we can change, add and remove items in a list after it has been created and it allows duplicate values
#accessing list items
print(mylist[0]) #first item
print(mylist[4]) #fifth item
print(mylist[-1]) #last item
print(mylist[1:4]) #slicing from index 1 to 3
#changing list items
list1 = ['orange', 'banana', 'cherry', 'apple', 'mango']
list1[2] = 'custard apple'
print(list1)
#this means we can change the value of the item using its index
#we can also change items using range of indices
list1[1:3] = 'kiwi', 'grape'
print(list1)
#2 adding list items
list1.append('watermelon')
print(list1) # it adds the element at the end of the list
list1.insert(0, 'pineapple')
print(list1) # it adds the element at the specified index
#extend() method to add elements of another list to the current list
list2 = ['peach' , 'plum']
list1.extend(list2)
print(list1)
#remove list items
list1.remove('orange')
print(list1)
#pop() method removes the specified index, if index is not specified it removes the last item
list1.pop(2)
print(list1)
list1.pop()
print(list1)
#del keyword to remove item at specified index
del list1[0]
print(list1)
#clear() method to remove all items from the list
list1.clear()
#loop lists usinng for loop
list1 = ['orange', 'banana', 'cherry', 'apple', 'mango']
for x in list1:
    print(x)
#looping through indices
for i in range(len(list1)):
    print(list[i])
#while loop
i = 0
while i <len(list1):
    print(list1[i])
    i+=1
#looping using list comphrension
for x in [x for x in list1]:
    print(x)
newlist = []
newlist = [x for x in range(10)]
print(newlist)
#sorting a list
list1 = ['orange', 'banana', 'cherry', 'apple', 'mango']
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
#copy a list
list2 = list1.copy()
print(list2)
list2 = list(list1)
print(list2)
#joining lists
list3 = list1 + list2
print(list3)
#list method() functions
#append() - adds an element at the end of the list
#clear()- removes all the elements from the list
#copy() - returns a copy of the list
#count() - returns the number of elements with specified value
#extend() - adds the elements of a list (or any iterable), to the end of the current list
#ndex() - returns the index of the first element with the specified value
#insert() - adds an element at the specified position
#pop() - removes the element at the specified position
#remove() - removes the item with the specified value
#reverse() - reverses the order of the list
#sort() - sorts the list

