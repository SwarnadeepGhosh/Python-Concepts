try:
    age = int(input('> '))
    2000/age  # Raise Zero division exception
    print(f"Age is {age}")
except ValueError:  # Handle Value exception
    print('Age must be integer')
except: 
    print ('Some other error occurred') # Handling Zero Division and other exceptions
else:
    print('No error occurred') # Will Run if no exception occurred