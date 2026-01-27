#Data structure is about how data can be stored in different structures
#algorithms is about how to slove different problems often by searching through and manipulating data structures
#data structures are the way of storing and organizing data in a computer
#python has built in data structure like list,tuple,set,dicitionary
#other data structures can be implemented using classes and onjects such as linked lists,stacks,queues,trees,graphs,hash tables
#data structures
#list and arrays
#stacks
#queues
#linked lists
#hash tables
#trees
#binary trees
#binary search trees
#avl trees
#heaps
#graphs
#ALGORITHMS
#linear search
#binary search
#bubble sort
#selection sort
#insertion sort
#quick sort
#counting sort
#radix sort
#merge sort
#dijkstra's algorithm
#depth first search
#breadth first search
#dynamic programming
#greedy algortihms
#ARRAYS
'''import array as arr
a = arr.array('i',[1,2,3,4,5])
print(a[2])
print(a[-1])
for x in a:
    print(x)
#changing the element
a[0] = 0
print(a)
#changing the element from 3rd position to 5th position
a[2:5] = arr.array('i',[10,11,12])
print(a)
#adding elements to an array
a.append(6)
print(a)
e = arr.array('d',[1.5,2.5,3.5])
f = arr.array('d',[7.3,7.5,9.1])
c = e + f
print(c)'''
#traversal
'''import array as arr
print("traversal of array :", end = " ")
a = arr.array('i',[10,20,30,40,50,60])
for i in a:
    print(i,end = " ")'''
'''import array as arr
a = arr.array('i',[1,2,3,4,5,])
ele = 21
a.append(ele)
for i in range(len(a)-1, -1, -1):
    print(a[i],end = " ")'''
'''import array as arr
bark = arr.array('i',[10,20,30,40,50,60])
del bark[2]
del bark[0]
bark.pop()
for j in range(len(bark)):
    print(bark[j], end = " ")'''
'''import array as arr
arr = [12,31,65,37,39,59]
key = 37
print('element found at index :', end = " ")
for i in arr:
    if i == key:
        print(arr.index(i),end = " ")
print()'''

#LINEAR SEARCH
'''def search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1
if __name__ == "__main__":
    arr = [10,20,38,91,31,50,78]
    n = 50
    result = search(arr,n)
    if(result == -1):
        print('element not found')
    else:
        print('element found at index :',result)'''
#fninding an index of an element in an unsorted array using linear search
'''def search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1
if __name__ == "__main__":
    arr = [12,34,56,78,90,47,91]
    n = 47
    result = search(arr,n)
    if result == -1:
        print('NF')
    else:
        print('element found at index', result)'''
#finding the occurance of an element in an array using linear search
'''def counting(arr,n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == n:
            count += 1
    return count
if __name__ == "__main__":
    arr = [1,21,42,21,63,21,69]
    n = 21
    result = counting(arr,n)
    if result == 0:
        print('element not found')
    else:
        print('element fount', result , 'times')'''
#finding the minimum and maximum element in an array using linear search
'''def min_max(arr,min,max):
    for i in range(len(arr)):
        return min(arr)
        return max(arr)
if __name__ == "__main__":
    arr = [12,21,67,87,10,8,91,17]
    result = min_max(arr,min,max)
    print('min element is :', min(arr))
    print('max element is :', max(arr))'''
'''def min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    minimum, maximum  = min_max(arr)
    print('minimum element is:', minimum)
    print('maximum element is:', maximum)'''
#to check if an array is sorted using linear search
'''def sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    result = sort(arr)
    if result == False:
        print('unsorted')
    else:
        print('sorted')'''
#to reverse an array using linear search
def reverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    reverse(arr)
    print(arr)