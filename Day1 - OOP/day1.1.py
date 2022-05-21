# Import only one function ( sqrt )
from math import sqrt

# Import all the functions from math ( using * )
from math import *

print("Hello again :)")

# String

name = "Shraddha didi :)"
# Integer
age = 50
# Floating
weight = 24.00
# Boolean
is_adult = True

print(name)
print(age)
print(weight)
print(is_adult)

# User input
myName = str(input("Enter a name : "))
# Concatination
print("Hello " + myName)


# Type conversion

# string to integer
# old_age = input("Enter your old age : ")
old_age = int(input("Enter your old age : "))
new_age = old_age + 2
print(new_age)

# Also you can convert in int(), str(), bool(), float()

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

sum = num1 + num2
print(f"Your sum is {sum}")


# STRING

name = "Tonny Stark"

# /# print(name.upper())
print(name.lower())
# Index always starts with 0 in python
print(name.find(" "))
# Not change in real string
print(name.replace("Tonny Stark", "Ironman"))
print("Tonny" in name)

# Operators

print(5000 + 2959)
print(546 - 464)
print(5 * 3)
print(5 / 2)
print(5 ** 3)
print(5 // 2)

# If-else statement you already know, right ?? :)


# Making Calculator using Python

userInput1 = int(input("Enter the first number : "))
userInput2 = int(input("Enter the second number : "))

print('''Write the operations you want like this,
1) + for Addtion,
2) - for Substraction,
3) * for Multiplication,
4) / for Division,
5) % for modules''')

userInput3 = input("Operation : ")

result = 0

if(userInput3 == "+"):
    result = userInput1 + userInput2

elif(userInput3 == "-"):
    result = userInput1 - userInput2

elif(userInput3 == "*"):
    result = userInput1 * userInput2

elif(userInput3 == "/"):
    result = userInput1 / userInput2

elif(userInput3 == "%"):
    result = userInput1 % userInput2

else:
    print("Sorry, we can't calculate!")

print(f"Your result is {result}")


# While loop

i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

i = 5
while i >= 0:
    print(i * "*")
    i = i - 1

# For loop

for i in range(5):
    print(i)


# LISTS
marks = [80, 94, 76, "Maths", "Science"]
print(marks)
print(marks[3])
print(marks[-1])
print(marks[1:3])
marks.append("Gujarati")
marks.remove("Gujarati")
print(marks)

for score in marks:
    print(score)

students = ["Harsh", "Darshan", "Jainish", "Kirtan", "Kushal", "Preet"]

for students in students:
    if students == "Kushal":
        break
        # continue
    print(students)


# TUPLE
# We cannot change the tuple items, but we change the list item
marks = (89, 98, 38, 78)
# marks[0] = 99
print(marks.count(98))
print(marks.index(98))
print(marks)


# DICTIONARY
person = {
    "Name": "Datt",
    "Age": 17
}
print(person.keys())
print(person.values())
print(person)


# MODULE FUNCTION ( MATH )
print(sqrt(16))


# Find average of two numbers using function
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def print_avg(num1, num2):
    result = num1 + num2 / 2
    print(result)

print_avg(num1, num2)