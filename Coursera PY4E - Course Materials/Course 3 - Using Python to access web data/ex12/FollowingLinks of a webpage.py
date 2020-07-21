# This program follows links at a given position for a given number of times and lists the resulting chain
'''
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the 
last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Romina.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the 
last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: C
'''

# Importing
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Initialising the count and total
name = list()

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking user to input parameters
url = input('Enter URL: ')
pos_str = input('Scanning for a tag that is at the following position relative to the first name in the list: ')
rep_str = input('Repeating the process to follow the link for the following number of times: ')

# Converting the inputs
position = int(pos_str)
repeat = int(rep_str)

# Looping through the layers of webpages 4 times
for repeat in range(repeat):
    # Reading the whole fine into a single long string
    html = urlopen(url, context=ctx).read()
    
    # Creating an organised string (soup) with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieving all of the 'a' tags
    tags = soup('a')
    
    # Adding the name of the person at the given position to the list
    name.append(tags[position-1].contents[0])
    
    # Updating the URL for the next loop
    url = tags[position-1].get('href', None)

# Printing the list with the names
print(name)

# Result
# ['Kahlya', 'Dre', 'Petra', 'Kassey', 'Richie', 'Mario', 'Carrie']
