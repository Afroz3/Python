#match statement is used to perform different actions based on different conditions
#instead of using many if else statements you can use the match statement
#match statements selects one of many code blocks to be executed
'''match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block '''
#how it works
#match expression is evaluated once
#the value of the expression is compared with the values of each case
# if there is a match the assosciated block of code is executed
day = input()
match day:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')