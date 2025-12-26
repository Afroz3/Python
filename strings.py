#strings are created using single or double quotes
single_quote = 'Hello'
double_quote = "world"
#multiple line strings can be created using triple quotes
multiline = '''this is a
multi-line
code in python'''
print(single_quote)
print(double_quote)
print(multiline)
print(type(single_quote))
#strings as arrays
#strings in python are unicode characters
#square brackers are used to access the elements of the string
print(single_quote[1])
#looping through a string
for ch in single_quote:
    print(ch)
#string length
#to getlength of a string len() function is used
print(len(multiline))
#check string
#to check if a character or substring is present in a string we use 'in' keyword
print('el' in single_quote)
#we can also use 'in' keyword in if statement
if 'el' in single_quote:
    print('yes,it is present in the string')
else:
    print('NA')
#check if not present
#we can use 'not in' keyword to check if a substring is not present in a string
print('key' not in single_quote)
#slicing strings
b = "python programming"
print(b[0:6])
print(b[:7])
print(b[7:])
print(b[:len(b)])
print(b[:5])
print(b[5:])
#negative indexing
print(b[-11:-1])
#modifying strings
#strings are immutable we cannot change the characters of a string but we can modify it by usng strind methods
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace('y','i'))
print(b.split(","))
#concatenate strings
x = "hello"
y = "world"
z = x+y
print(z)
#joining string which have spaces in between
c = ["python", "is", "a", "programming", "language"]
print(" ".join(c))
#string format
#as we cannot concatenate strings and numbers directly with + operator so we use format() method to combine different data types
age = 22
txt = f'iam {age} years old'
print(txt)
price = 49.2345
txt2 = f"the price is {price:.2f} rupees"
print(txt2)
#escape characters
#to insert characters that are illegal in a string we use escape characters with backslash \
escape_str = 'we are so called \'professionals\''
print(escape_str)
#escape sequences
#\n - new line
#\t - tab
#\\ - backslash
#\r - carriage return
#\b - backspace
#\f - form feed
#\ooo - octal value
#\xhh - hexadecimal value
print("hello\nworld")
print("hello\tworld")
print("this is a backslash\\")
print("hello\rworld")
print("hello\bworld")
print("hello\fworld")
print("octal value: \110\145\154\154\157")
print("hexadecimal value: \x48\x65\x6c\x6c\x6f")
#string methods
str1 = "     hello world"
print(str1.capitalize())
print(str1.casefold())
print(str1.center(20))
print(str1.count('l'))
print(str1.encode())
print(str1.endswith('d'))
print(str1.expandtabs(10))
print(str1.find('w'))
print(str1.index('d'))
print(str1.isalnum())
print(str1.isalpha())
print(str1.isascii())
print(str1.isdecimal())
print(str1.isdigit())
print(str1.isidentifier())
print(str1.islower())
print(str1.isnumeric())
s = 'python', 'programming', 'language'
print(' '.join(s))
print(str1.isprintable())
print(str1.isspace())
print(str1.istitle())
print(str1.isupper())
print('#'.join(s))
print(str1.ljust(30))
print(str1.lstrip())
print(str1.maketrans('h', 'P'))
txt = 'I could eat bananas all day'
print(txt.partition('bananas'))
print(str1.replace('h', 'P'))
print(str1.rfind('o'))
print(str1.rindex('d'))
print(str1.rjust(30))
print(str1.rstrip())
print(str1.split())
print(str1.splitlines())
print(str1.strip())
print(str1.swapcase())
print(str1.translate(str1.maketrans('h','p')))
print(str1.zfill(50))