# # Firstly, let's make hello world program
print("Hello World!")

#
# '''
#     This is multiline comment
# '''
#

str = "This is a string!"
print(str)


age = 17
print(age)

weight = 46.90
print(weight)

# Basic Operations
print("The value of 3 + 5 is ",3 + 5)
print("The value of 3 - 5 is ",3 - 5)
print("The value of 3 * 5 is ",3 * 5)
print("The value of 3 / 5 is ",3 / 5)
print("The value of 3 ** 5 is ",3 ** 5)
print("The value of 3 // 5 is ",3 // 5)

multilineStr = '''
    This is a multiline string
    Okay!
'''
print(multilineStr)

print("%s to the right " %{"This is a string"})

# F string
age = 17
print(f"My age is {age}")

# Lists
colleges = ['BBIT', 'DDIT', 'IIT']
print(colleges)
colleges[2] = 'NIT'

# Index start from 0
print(colleges[2])

# Get items from ranges
print(colleges[1:3])

# Append items
colleges.append('SPU')
print(colleges)

# Remove items
colleges.remove('SPU')
print(colleges)

# Get datatype
print(type(colleges))

# Get length of list
print(len(colleges))

# Max is IIT, And Min is BBIT, Because in dictionary BBIT is on first and then we get IIT
print(max(colleges))
print(min(colleges))

# Tuple : We cannot change the elements of tuple, but we can change the elements of any list
# If you change the element of tuple, then first you have to convert it into the list and then you can
# change the item and after that again convert it into a tuple

tup1 = (1, 2, 3)
print(tup1)
print(type(tup1))

# Not possible
# tup1[0] = 3
# print(tup1)

# Dictionary
names = {
    "Name": "Datt Panchal",
    "Age": 17,
    "Role": "Student | Coder | Learner"
}
print(names)

# Get keys and values
print(names.keys())
print(names.values())


# If- else statement
# it takes input in form of string
getNum = input("Enter the number : ")

# If you take the input in form of numbers, run this!
getNum2 = int(input("Enter the marks: "))
print(getNum2)

if(getNum2 <= 40):
    result = "Fail"
    print(result)

elif(getNum2 <= 60 and getNum2 > 40 ):
    result = "Second Class"
    print(result)

elif(getNum2 <= 80 and getNum2 > 60):
    result = "First class"
    print(result)

elif(getNum2 <= 100 and getNum2 > 80):
    result = "Dict!"
    print(result)

else:
    print("Sorry, nothing to show!")


# LOOPS
num = int(input("Enter the number : "))
for i in range(num):
    print(i)

list = [['Civil, Electrical'] ,['Civil, Electrical']]
for item in list:
    for i in item:
        print(i)


# FUNCTIONS
# find average function
def average(num1, num2):
    return (num1 + num2)/2

print(average(2, 3))

# find sum of numbers
def sum(num1, num2):
    return num1 + num2

print(sum(4, 5))


# STRING FUNCTION
myStr = "Datt Panchal"
print(myStr[0:4])
print(myStr[-2:])
print(myStr[:])
print(myStr.capitalize())
print(myStr.upper())
print(myStr.lower())
print(myStr.find("Datt"))


# FILE HANDLING IN PYTHON

# Open file and write something in file
file1 = open("dummy.txt", "wb")
print(file1.name)
print(file1.mode)
file1.write(bytes("Hello datt!", "UTF-8"))
file1.close()

#  Reading the content of the file
file2 = open("dummy.txt", "r+")
text_to_read = file2.read()
print(text_to_read)
file2.close()


# OBJECT ORIENTED PROGRAMMING ( OOP ) Practicing Examples

class Employee:

    # Here, double underscore ( __ ) means it is a private varible
    __name = None
    __id = 0
    __salary = 0

    # Creating constructor
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    # Setter
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_salary(self, salary):
        self.__salary = salary

    # Getter
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_salary(self):
        return self.__salary

# Directly set values through the constructor
dattu = Employee("Datt Panchal", 39, 5000000)

# Set items
dattu.set_name("Datt Panchal")
dattu.set_id(39)
dattu.set_salary(50000)

# Get items
print(dattu.get_name())
print(dattu.get_id())
print(dattu.get_salary())