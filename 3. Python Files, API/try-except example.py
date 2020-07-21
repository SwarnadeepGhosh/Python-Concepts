import requests
# Basic Exception handling example
'''
x = int(input('Enter a number : \n'))
try:
    y = (10/x)
    print(y)
except ZeroDivisionError:
    print('Cant divide by zero')
'''

# Internet Connection Error Exception handling example
try:
    r = requests.get("https://www.udacity.com")
    print(r) # If you did print(r.status_code), that also works!
except requests.exceptions.ConnectionError:
    print("Could not connect to server.")