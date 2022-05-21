# Map, Filter and Reduce

# MAP FUNCTION

# The Map function is used to apply any function in a list. To convert list element which is in form of string into integer, the map function is used. It's returns one object.
# Lambda Function : It is a one line of function which returns something

numbers = ["5", "2", "5"]

# To convert list element which is one string into integer
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# But using for loop it is not efficient way, using map function it is do above working in just one line
numbers = list(map(int, numbers))

numbers[1] = numbers[1] + 3

print(numbers)


# Finding squares of the number using map function and lambda function

num = [1, 2, 3, 4, 5]

# Simple function
def sq(a):
    return a*a

find_square = list(map(lambda a: a*a, num))

print(find_square)


# Finding squares and cubes of numbers using diffrent method

def sq(a):
    return a*a

def cube(a):
    return a*a*a

i = 0

def inc(i):
    i = i + 1
    return i

func = [inc, sq, cube]

for i in range(6):
    result = list(map(lambda x:x(i), func))
    print(result)


# FILTER FUNCTION : It making a list of elements on which the specific / given function returns a True

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_than_5(num):
    return num > 5

gr_than_5_var = list(filter(is_greater_than_5, list_1))
print(gr_than_5_var)


# REDUCE

# Reduce is a part of functools module.

from functools import reduce

list_2 = [1,2,3,4]

# Adding and Multiply the list_2 elements using reduce() and lambda function
Addition_result = reduce(lambda x,y:x+y, list_2)
Multiplication_result = reduce(lambda x,y:x*y, list_2)

print(Addition_result)
print(Multiplication_result)


