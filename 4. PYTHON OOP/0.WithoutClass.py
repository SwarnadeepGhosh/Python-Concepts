class Employee:
    pass

# All Employees are similar so we made them from Employee template. 
harry = Employee()
rohan = Employee()

# Methods & Attributes are used to set name, email, salary etc.
# Functions are used to increase salary to Specific employee

# Without Using class 
harry.fname = 'harry'
harry.lname = 'jackson'
harry.salary = 44000

rohan.fname = 'rohan'
rohan.lname = 'das'
rohan.salary = 4000

print(harry.salary)  #Outputs 44000