'''


You can test to see if your program is working with a location of "South Federal University" which will have a 
place_id of "ChIJoyahebsD2YgRoOqYC_zKBPU".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2154 characters
Place id ChIJoyahebsD2YgRoOqYC_zKBPU
Turn In

Please run your program to find the place_id for this location:

University of West Florida
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The 
first seven characters of the place_id are "ChIJ1y1 ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work 
with the Google API - but the place_id may not match for this assignment.
'''
#===============================================================================
# This programme reads an online JSON file from which it extracts the first
# "place_id", which uniquely identifies a place on Google Maps
#===============================================================================


# Importing libraries
import urllib.request, urllib.parse, urllib.error
import json
#api_key = False

'''
if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else :
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
'''
# Initialising
service_url = 'http://py4e-data.dr-chuck.net/geojson?'

# Asking user to input the source URL of the JSON data file
loc = input('Enter location: ')

# Concatinating the URL for the request
url = service_url + urllib.parse.urlencode({'address' : loc}) 
print('Retrieving', loc, 'here:', url)

# Opening connection to the JSON data file
uhandle = urllib.request.urlopen(url)
data = uhandle.read().decode()
print('Retrieved', len(data), 'characters')
 
# Transforming the text of the JSON file into a tree
try:
    tree = json.loads(data)
except:
    tree = None
 
# Finding the first "place_id" in the JSON data file
place_id = tree["results"][0]["place_id"]
 
# Printing the result
print('Place ID:', place_id)

# Retrieved 2187 characters
# Place ID: ChIJWWcAJ8nAwogRKfVGTRp9CNk
