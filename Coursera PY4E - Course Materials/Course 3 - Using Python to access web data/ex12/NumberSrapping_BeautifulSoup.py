# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_408965.html (Sum ends with 51) 

# This program scrapes a website for numbers and returns their count and sum.

# Importing
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Initialising the count and total
total=0
count=0

# Asking user to input the URL
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

# Creating an organised string (soup) with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    try:
        total = total + int(tag.contents[0])
        count = count + 1
    except:
        continue
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

# Printing the result
print('Count:',count)
print('Sums=',total)

# Result
# Count: 50
# Sums= 2351
