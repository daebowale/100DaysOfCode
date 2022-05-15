'''

What is Object Oriented Programming ?

- You know you are surrounded with objects. To represent this object in programming world means our main
task is we have to work with real world entities in programming. So, that is why object oriented
programming comes in.

What is Classes ?

- Class is a templates / blue prints of real world entities ( Objects )
- Class is a user defined data type.

What is objects ?

- Objects are specific instances of a class.

Constructor : Init method acts as a Constructor

Inheritance : With inheritance one class can derive the properties of anather class

Types of inheritance :
 1) Single Inheritance
 2) Multiple Inheritance
 3) Multi-level Inheritance : We have Parent, Child, grand-child relationship
 4) Hybrid Inheritance

'''


# Creating a class example 1

# class Phone:

    # Creating methods

    # def make_call(self):
    #     print("Making a call!")
    #
    # def making_game(self):
    #     print("Making a game")

# create a object of class
# obj1 = Phone()

# obj1.make_call()
# obj1.making_game()


# Creating class example 2

# class Phone:

#     def set_color(self, color):
#         self.color = color

#     def set_cost(self, cost):
#         self.cost = cost

#     def get_color(self):
#         return self.color

#     def get_cost(self):
#         return self.cost


# obj1 = Phone()

# obj1.set_color("Blue")
# obj1.set_cost(50000)

# print(obj1.get_color())
# print(obj1.get_cost())


# Creating class example 3 with constructor concept

# class Employee():

#     def __init__(self, name, age, gender, role, salary):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.role = role
#         self.salary = salary

#     def get_details(self):
#         return print(f'''The name of the employee is {self.name} and the age is {self.age}. Gender is {self.gender}. His role is {self.role} and his salary is {self.salary}!''')


# employeeObj = Employee("Unknown", 17, "Male", "Web Developer", 1000000)

# Employee.get_details(employeeObj)


# Creating class example 4 with Inheritance concept

# class Vehicle():

#     def __init__(self, name, mileage, cost):
#         self.name = name
#         self.mileage = mileage
#         self.cost = cost

#     def get_details(self):
#         print(f'''The name of the car is {self.name} and his mileage is {self.mileage}. And the cost is {self.cost}''')

# class Car(Vehicle):

#     def show_slug(self):
#         print("Best Car!")


# carObj = Car("Tesla", 500, 100000)

# carObj.get_details()
# carObj.show_slug()



# Creating class example 5 with over-riding the init method ( Taking same example of car )

# class Vehicle():

#     def __init__(self, name, mileage, cost):
#         self.name = name
#         self.mileage = mileage
#         self.cost = cost

#     def get_details(self):
#         print(f'''The name of the car is {self.name} and his mileage is {self.mileage}. And the cost is {self.cost}''')
#
# class Car(Vehicle):

#     def __init__(self, name, mileage, cost, tyres, hp):
#         super().__init__(name, mileage, cost)
#         self.tyres = tyres
#         self.hp = hp

#     def get_other_details(self):
#         return print(f"Extra Info: Number of tyres are {self.tyres} and hours/power is {self.hp}.")

# carObj = Car("Tesla", 500, 100000, 4, 500)

# carObj.get_details()
# carObj.get_other_details()



# Creating classes with Multiple Inheritance Concept

# class Parent1():

#     def str1(self, str1):
#         self.str1 = str1

#     def show_str1(self):
#         return self.str1

# class Parent2():

#     def str2(self, str2):
#         self.str2 = str2

#     def show_str2(self):
#         return self.str2

# class Child(Parent1, Parent2):
#     def str3(self, str3):
#         self.str3 = str3

#     def show_str3(self):
#         return self.str3

# showStrObj = Child()

# showStrObj.str1("This is a first string from Parent1")
# showStrObj.str2("This is a second string from Parent2")
# showStrObj.str3("This is a third string from Child")

# print(showStrObj.show_str1())
# print(showStrObj.show_str2())
# print(showStrObj.show_str3())



# Creating classes with Multi-level Inheritance

# Parent Class
# class Grandfather():
#
#     def assign_name1(self, name1):
#         self.name1 = name1
#
#     def show_name1(self):
#         return self.name1
#
# # Child Class
# class Father(Grandfather):
#
#     def assign_name2(self, name2):
#         self.name2 = name2
#
#     def show_name2(self):
#         return self.name2
#
# # Grand-Child Class
# class Son(Father):
#
#     def assign_name3(self, name3):
#         self.name3 = name3
#
#     def show_name3(self):
#         return self.name3
#
# MultiLevelObj = Son()
#
# MultiLevelObj.assign_name1("I'm a GrandFather")
# MultiLevelObj.assign_name2("I'm a Father")
# MultiLevelObj.assign_name3("I'm a Son")
#
# print(MultiLevelObj.show_name1())
# print(MultiLevelObj.show_name2())
# print(MultiLevelObj.show_name3())


# Creating the class example 6 with more example with constructor

# class EBranch():
#
#     def __init__(self, name, years, future):
#         self.name = name
#         self.years = years
#         self.future = future
#
#     def get_branches(self):
#         print(f"The name of the branch is {self.name} and the years to do that is {self.years}. The future in this field is {self.future}")
#
# branchObj = EBranch("Computer Engineering", 3, "Best Future!")
#
# branchObj.get_branches()
#
# # Apply inheritance with the same above example
#
# class acs(EBranch):
#
#     def __init__(self, name, years, future, best_teacher):
#         super().__init__(name, years, future)
#         self.best_teacher = best_teacher
#
#     def get_others_info(self):
#         print(f"The best teacher of this field is {self.best_teacher}")
#
# acsObj = acs("EC", 3, "Best", "Kunal J. Pithdiya")
#
# acsObj.get_branches()
# acsObj.get_others_info()