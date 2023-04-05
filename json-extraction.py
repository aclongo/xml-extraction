# The program will prompt for a URL,
# read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file

import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try: # prompt the user for a url location and read it with urllib
        url = input('Enter location: ')
        data = urllib.request.urlopen(url, context=ctx).read()
        break
    except: # prevent invalid urls from crashing the program
        print('Invalid url. Try again.')
        continue

print('Retrieving', url) # let the user know retrieval was successful
print('Retrieved', len(data), 'characters') # get the total number of characters in the file

js = json.loads(data)

# Access the comment section and count them
info = js['comments']
comments = len(info)
print('Count:', comments)

sum = 0
# Iterate through each comment and extract the count
for item in info:
    count = item['count']
    sum += int(count) # add to the total sum

print('Sum:', sum)