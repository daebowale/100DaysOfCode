class Employee():

    # Main Class Variable
    increaseSalary = 2

    # Creating Constructor
    def __init__(self, fname, lname, salary):

        # Instance Variables
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # Function to increase the salary
    def increase_salary(self):
        self.salary = self.salary * self.increaseSalary

    # Specifying one Dunder method
    def __add__(self, other):
        return self.salary + other.salary

    # Some Magic Functions

    # Specifying __repr__ dunder method
    def __repr__(self):
        return 'Employee({}, {}, {})'.format({self.fname}, {self.lname}, {self.salary})

    # Specifying __str__ dunder method
    def __str__(self):
        return 'Name is {} {}'.format({self.fname}, {self.lname})

    # Function to get details of the employee
    def get_details(self):
        print(f"The name of the person is {self.fname} {self.lname} and the his salary is {self.salary}!")


employeeObj1 = Employee("Sam", "jackson", 100000)
employeeObj2 = Employee("Michel", "jackson", 100000)

# To see the instance variables of the class
print(employeeObj1.__dict__)

# Using Dunder method, add two object's salaries
print(employeeObj1 + employeeObj2)

# Print statment when we print any object using __repr__
print(repr(employeeObj1))

# Print statement when we print any object using __str__
print(str(employeeObj2))

employeeObj1.get_details() # Salary is 100000
employeeObj1.increase_salary() # After execution
employeeObj1.get_details() # Salary is 200000
