# MORE ON ITERTOOLS

'''

What is Iterator ?

- An Iterable is basically a sequence that will be converter into an iterator. Like a Tuple
List, String etc.
- The Iterator can be using the iter()
- To iterate we can use next() or a for loop

What is itertools ?

- Python itertools provides tools and methods to create a iterator with efficiency

Python itertools methods

1. Infinite iterator
2. Iterators terminating on the shortest input sequence
3. Combinatoric iterators

'''

# ------------------------------------------------------------------
from itertools import *
import operator

list1 = [1,2,3,4,5]

iteratorObj = iter(list1)

# First way to iterate a list

op = next(iteratorObj)
op = next(iteratorObj)
op = next(iteratorObj)
op = next(iteratorObj)
op = next(iteratorObj)
print(op)

# Second way to iterate a list
for num in list1:
    print(num)

# ------------------------------------------------------------------
# Infinite Iterators

a = count(0, 2)
a = cycle([1,2,3,4,5]) # It is copying elements from iterable which is a
a = repeat(10) # It repeats & repeats number 10 nine times, at the 10 time the loop will break here

d = 0
for i in a:
    if d > 9:
        break
    else:
        print(i)
    d += 1


# ------------------------------------------------------------------
# shortest input sequence
# ------------------------------------------------------------------
a = [1,2,3,4,5]
# accumulate is returns a accumulated sum of the elements in iterable
b = accumulate(a)
b = accumulate(a, operator.mul)
b = accumulate(a, operator.xor)

for i in b:
    print(i)

# ------------------------------------------------------------------
a = [1,2,3,4]
b = [5,6,7,8]

# Join two or more iterators using chain()
a = chain(a, b)

for i in a:
    print(i)

# ------------------------------------------------------------------
# Compress
a = [1,2,3,4]
selector = [1]
selector = [1,0,1]

a = compress(a, selector)

for i in a:
    print(i)


# ------------------------------------------------------------------
# dropwhile : It returns when function returns false

a = list(range(0, 100, 5))
b = dropwhile(lambda x:x<20, a)

# Same as dropwhile
b = filterfalse(lambda x:x<20, a)

for i in b:
    print(i)


# ------------------------------------------------------------------
# islice
b = islice(a, 0, 15, 3)

for i in b:
    print(i)

print(a)

# ------------------------------------------------------------------
# starmap
a = [(1,2), (3,4), (5,6), (7,8)]
b = starmap(lambda x,y:x+y, a)
b = starmap(lambda x,y:x*y, a)

for i in b:
    print(i)

# ------------------------------------------------------------------
# takewhile - Opposite of dropwhile. It returns when function returns true

a = list(range(0, 100, 5))
b = takewhile(lambda x: x < 20, a)

for i in b:
    print(i)

# ------------------------------------------------------------------
# tee()
a = [1,2,3,4,5]
ite = iter(a)
b = tee(ite, 5)

for i in b:
    print(i)
    print(list(i))

# ------------------------------------------------------------------
# zip_longest()
a = [1,2,3,4]
b = [5,6,7,8]

c = zip_longest(a,b)

for i in c:
    print(i)

# ------------------------------------------------------------------
# group by
a = [(1,2), (3,4), (5,6), (7,8)]

func_key = lambda x : x[1]

b = groupby(a, func_key)

for i,j in b:
    print(i, list(j))

# ------------------------------------------------------------------
# Combinations : Bunch of methods like product()
a = product('XYZ', repeat=2)
a = permutations('XYZ', 2)
a = combinations('XYZ', 2)
a = combinations_with_replacement('XYZ', 2)

for i in a:
    print(i)
