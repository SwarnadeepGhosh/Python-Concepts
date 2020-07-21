#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_408963.txt (There are 78 values and the sum ends with 538)

# Importing the regex library
import urllib.request, urllib.parse, urllib.error
import re

# Asking user to enter the source file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_408963.txt"
# Opening the source file
fhandle = open(fname)
#fhandle=urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_408963.txt')
#fhandle=str(fhandle).decode

# Initialising the sum of the numbers
total = 0

# Reading file line-by-line
for line in fhandle:
    # Finding all the numbers as strings into listOfNums
    listOfNums = re.findall('([0-9]+)', line.rstrip())
    # If there is not any number in a line go to the next loop...
    if len(listOfNums) < 1 :
        continue
    else :
        # ... else looping through the list of numbers found...
        for snum in listOfNums :
            # ... and add up the converted numbers
            total = total + int(snum)

# Printing the sum of the numbers
print(total)

#sum=357538
