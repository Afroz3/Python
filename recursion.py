#recursion
#it is a function which calls itself
#recursion is a common mathematical and programming concept.it means that a function calls itself. this has benefit of meaning that you can loop through data to reach a result
#a simple recursion can count down from 5
'''def countdown(n):
    if n <= 0:
        print('done')
    else:
        print(n)
        countdown(n-1)
countdown(5)'''
#base case and recursive case
#every recursive function must have two parts
#1 base case - A condition that stops the recursion
#2 recursive case - function calling itself with modified argument
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))'''
#fibonacci series
'''def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))'''
'''def sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum(numbers[1:])
my_list = [1,2,3,4,5]
print(sum(my_list))'''
'''def max(numbers):
    if numbers == 1:
        return numbers[0]
    else:
        max_list = max(numbers[1:])
        return numbers[0] if numbers[0] > max_list else max_list
my_list = [3,4,6,7,8,9]
print(max(my_list))'''
