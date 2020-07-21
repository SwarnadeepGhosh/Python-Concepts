# We will increase code reusability by class
class Employee:
    # class variable
    increment = 1.5
    no_of_employees = 0
    # initialise constructor
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.2
        Employee.no_of_employees += 1

# normal method
    def increase(self):
        self.salary = int(float(self.salary) * Employee.increment)

# class methods takes whole class as a argument.
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

# Creating different employees from Employee template
harry = Employee('harry','jackson','44000')
rohan = Employee('rohan','das','64000')

print(harry.salary)  #Outputs 44000
# harry.increase()
Employee.change_increment(2)
harry.increase() #automatically takes self as a argument
print(harry.salary) #Outputs 88000
