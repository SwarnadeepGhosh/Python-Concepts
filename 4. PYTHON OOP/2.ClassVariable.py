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


    #def increase(self):
        #self.salary = int(float(self.salary) * self.increment)

print(Employee.no_of_employees) # Output: 0
# Creating different employees from Employee template
harry = Employee('harry','jackson','44000')
rohan = Employee('rohan','das','64000')
print(Employee.no_of_employees) # Output: 2

# print(harry.salary)  #Outputs 44000
# harry.increase()
# print(harry.salary) 
# print(harry.__dict__)
# print(Employee.__dict__)