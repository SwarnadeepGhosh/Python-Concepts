# This programme reads an online JSON file from which it extracts the values of the "count" items and sums those values

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_408968.json (Sum ends with 62)

# Importing libraries
import urllib.request, urllib.parse, urllib.error
import json

# Initialising
total_count = 0

# Asking user to input the source URL of the JSON data file
url = input('Enter URL: ')
print('Retrieving',url)
uhandle = urllib.request.urlopen(url)
data = uhandle.read()

# Transforming the text of the JSON file into a tree
tree = json.loads(data)

# Looping through all the comments under the "comments" item
for comment in tree['comments']:
    # Converting the text of the "count" items into an integer and summing
    try:
        total_count = total_count + int(comment['count'])
    except:
        continue

# Printing the result
print('Retrieved',len(data),'characters')
print('Count:',len(tree['comments']))
print('Sum:',total_count)

# Retrieved 2726 characters
# Count: 50
# Sum: 2362
