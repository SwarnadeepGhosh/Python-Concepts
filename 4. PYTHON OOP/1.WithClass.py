# We will increase code reusability by class
class Employee:
    # initialise constructor
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

# Creating different employees from Employee template
harry = Employee('harry','jackson','44000')
rohan = Employee('rohan','das','64000')

print(harry.fname)  #Outputs 44000