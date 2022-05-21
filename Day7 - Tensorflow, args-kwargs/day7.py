# *args and **kwargs in Python
# -----------------------------------------------------

# Simple function

def func(a,b,c,d):
    print(a,b,c,d)

func("Datt", "Ayush", "Kunal", "Arjun")

# *args example

# Please write the normal argument first and then write the args argument
def funcArgs(marks, *args):
    # the list (myNames) come here as a tuple
    print(type(args))
    print(args[0])
    print(marks)

    # Iterate using for loop
    for i in args:
        print(i)

myNames = ["name1", "name2", "name3", "name4"]
marks = [90,79,90,68,70]

funcArgs(marks, *myNames)


# *kwargs example

# Please write the normal argument first and then write the args argument
def funcArgs(marks, *args, **kwargs):
    # the list (myNames) come here as a tuple
    print(type(args))
    print(args[0])
    print(marks)

    # Iterate using for loop
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(f"The key is {key} and his value is {value}")

myNames = ["name1", "name2", "name3", "name4"]
marks = [90,79,90,68,70]

kw = {"Name": "XYZ", "Age": "999"}

funcArgs(marks, *myNames, **kw)

