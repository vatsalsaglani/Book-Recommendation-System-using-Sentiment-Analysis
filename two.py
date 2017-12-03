import pyrebase
from pprint import pprint 
from operator import itemgetter
import time
import requests
import json
import serial
config = {
  "apiKey": "Your Stuff",
  "authDomain": "Your Stuff",
  "databaseURL": "Your Stuff",
  "storageBucket": "Your Stuff"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
res = db.child("Admin").get().val()
g = input("Genre: ")

results =[]
result2 = []
for x in res.items():
	if(x[1]["genre"]==g):
		results.append((x[1]['book'],x[1]["score"]))
		
x = sorted(results,key=itemgetter(1))
for y in res.items():
	if(y[1]["genre"]==g):
		result2.append((y[1]['book'],y[1]["rating"]))
		
y = sorted(result2,key=itemgetter(1))
b = list(x)
b.reverse()

a = list(y)
a.reverse()


pprint('Books according to the best Ratings:')
pprint(a)
print("\n")
pprint('Books according to Sentiment Analysis Score:')
pprint(b)
#pprint(x)
#pprint(res.items()[0][1]["genre"])
#pprint(y)
#pprint(res.items()[0][1]["rating"])
