##########################################
###     Using Web Services             ###
###     Updated: 9/7/22                ###
##########################################

#####################
###XML- extensible markup language
#####################

#looks very similar to HTML, but is more structured.

#example:
#<person>
#    <name>Chuck</name>
#    <phone type="intl">
#        +1 734 303 4456
#    </phone>
#    <email hide="yes" />
#</person>

#each pair of opening and closing tags represent
#element or node with the same name of the tag

#each element can have some text or attributes

#####################
###Parsing XML
#####################

import xml.etree.ElementTree as ET

#create the data. triple quotes allow for strings
#on multiple lines

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

#from string converts the string into a tree of XML elements
#which allows for parsing using built-in functions
tree = ET.fromstring(data)

#asking python to find the name and email
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#####################
###Looping through nodes
#####################

#new data
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

#convert to tree
stuff = ET.fromstring(input)

#find all users
lst = stuff.findall('users/user')

#count users
print('User count:', len(lst))

#print name of user and, id, and x value
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

#check out this simple mistake if we input the wrong findall
lst = stuff.findall('users/user')
print('User count:', len(lst))

lst2 = stuff.findall('user')
print('User count:', len(lst2))

#####################
###JSON-javascript object notation
#####################

#inspired by the object and array format in JS

#python was invited before, and influenced JSON format

#example encoding:
    #{
        #"name" : "Chuck",
        #"phone" : {
            #"type" : "intl",
            #"number" : "+1 734 303 4456"
            #},
            #"email" : {
            #"hide" : "yes"
        #}
    #}

#####################
###Parsing JSON
#####################

#JSON is constructed by nesting dictionaries and
#lists as needed

#first example: list of users as dictionary

import json


data = '''
[
    { "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    } ,
    { "id" : "009",
        "x" : "7",
        "name" : "Brent"
    }
]'''

#load the data to break it into pieces
info = json.loads(data)

#parse element and count
print('User count:', len(info))

#loop through and print parsed values
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

#####################
###Application Programming Interfaces- APIs
#####################

#now we've built skills to exchange data between
#sites using HTTP, and a way to represent the 
#complex data found on the internet in a easy way

#next, we need to be able to document the connections
#between apps. These are APIs, which allow us to 
#make a set of services available for use by other
#apps and publishes the APIs (aka. rules) for access

#When building programs that rely on other services
#hosted by other programs, we can call this as 
#service-oriented architecture (SOA). 
#image search architecture

#Many advantages:
    #only need to maintain one copy of data
    #owner of the data can set the rules about data

#when app makes a set of services in its API over the web,
#we can these WEB SERVICES
    #Think about AWS- amazon web services, which owns
    #90% of the internet


#####################
###Application Example 1: Google Geocoding
#####################

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

