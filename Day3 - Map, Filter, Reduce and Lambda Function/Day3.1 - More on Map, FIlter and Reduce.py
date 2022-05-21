# MAP FUNCTION

# map(function_to_apply, list_of_inputs)

# Finding square of the list's elements
list1 = [1,2,3,4,5]

def sq(a):
    return a*a

sqResult = list(map(sq, list1))
print(sqResult)


# FILTER FUNCTION

# Return True if number is less than 5 in a list2
def less_than_5(num):
    return num < 5

list2 = [1,2,3,4,5,6,7,8,9]

result = list(filter(less_than_5, list2))
print(result)


# REDUCE

from functools import reduce

list3 = [1,2,3,4,5]


def sum_nums(a, b):
    return a + b


result2 = reduce(sum_nums, list3)
print(result2)
