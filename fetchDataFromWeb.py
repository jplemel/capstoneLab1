#Get the rating for a particular movie from OMDB
#http://www.omdbapi.com/
import urllib
from urllib import request
#Import request module
#cant install requests
#import requests

import json

resp = request.urlopen("http://www.omdbapi.com/?t=frozen&y=&plot=short&r=json")


json_data = resp.read().decode()

json_object = json.loads(json_data)

#print(json_object)
print(json_object['imdbRating'])

#Now, we have a Response object called r
#We can get all the information we need from this object.
#r = requests.get('http://www.omdbapi.com/')
#make request to the website
#


#get data as JSON
#//jsonR = r.json()

#process data to extract the data you need

#ERROR HANDLING: access denied, no network connection, invalid response...
#print(r)
