
# EXCEPTION HANDLING ( Try and Except Handling )
# ----------------------------------------------------------------

# Inputs the numbers from the user

num1 = input("Enter a number 1 : ")
num2 = input("Enter a number 2 : ")

# Try that this is execute or not. if error occurs, print the error statement as a string and then continue the program
try:
    # Error will occur in this print statement
    print("The sum of num1 and num2 is", int(num1) + int(num2))

    # Error will not occur in this print statement
    print("The sum of num1 and num2 is", num1 + num2)

# If error occur then print an error
except Exception as e:
    print(e)

# This print statement is always execute
print("This statement is execute the try block!")


# ------------------------------------------------------------------
# DECORATORS IN PYTHON

# Create a function1
def func1():
    print("Hello!")

# Function 1 is now equal to the function 2
func2 = func1

# Delete function1
del func1

# Run function2. It is execute! Why ? We are deleted the function1. Then why it is return "Hello!"?
# Because now one another copy is created of function 2

func2()

# Create another function

def funcRet(num):
    if num == 0:
        return print
    elif num == 1:
        return sum
    else:
        return print("Sorry!")

result = funcRet(5)
print(result)


# Create function in function as an argument. And using function we return another function

def executor(func):
    func("This is me:)")

executor(print)


# Example of Decorator

def firstFunction(otherFunction):
    def nowExecute():
        print("First print this!")
        otherFunction()
        print("And Third print this!")
    return nowExecute

@firstFunction
def myFunc():
    print("Second print this!")

# Instead of @firstFunction, you can also run this
myFunc = firstFunction(myFunc)

myFunc()

# ------------------------------------------------------------------
# ITERATOR, ITERABLE, ITERATION AND GENERATORS IN PYTHON

# ITERABLE : It is a python object in which __iter__() or __getitem__() methods will define. It generates iterator. String is also a iterable.
# ITERATOR : It is a python object in which  __next__() will define.
# ITERATION : It is a process to iterate.
# GENERATORS : It is a one type of iterators. You can iterate it only for one time. Range() is a also one generator.


def gen(n):
    for i in range(n):
        # This is not a function, this is one generator.
        yield i

g = gen(5)
# Generate now
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

# Generate using For loop
for i in g:
    print(i)

# Iterable example
# integer object is not iterable
str = "Unknown"
ite = iter(str)
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())

# Using loop
for char in str:
    print(char)


# ------------------------------------------------------------------
# REGULAR EXPRESSION ( RagEx )
# re is a module which help us to incorporate the Ragular Expression

import re

myStr = '''My name is XYZ. I am 999 years old. I am belongs to Mars. We will waiting for you man.
Please tell to Elon Musk, we are waiting for you'''

'''
Functions in RegEx
- findall
- search
- split
- sub
- finditer
'''

# Here is Raw string
# Meta Characters

# find 'XYZ' in myStr
pattern = re.compile(r'XYZ')

# . means Any character. It is a meta character
pattern = re.compile(r'.')

# If myStr starts with My name, then it returns
pattern = re.compile(r'^My name')

# If myStr ends with you, then it returns
pattern = re.compile(r'you$')

# Zero or more occurances
pattern = re.compile(r'we*')

# One or more occurances
pattern = re.compile(r'w+')

# Exactly the specified number of occurances
pattern = re.compile(r'we{2}')

# Capture and group
pattern = re.compile(r'(we){2}')

# Either or
pattern = re.compile(r'we{1}|are')

# Special sequences

# Return when the char on beginning of string
pattern = re.compile(r'\AMy')

# Return when the others char starts in string
pattern = re.compile(r'\bI')

# Same as for ends with using \b after string
# So many special sequences are available, you can find on online

matches = pattern.finditer(myStr)

for match in matches:
    print(match)
    print(myStr[11:14])





