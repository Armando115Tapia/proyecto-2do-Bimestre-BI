#Código escrito en Python semejante al archivo harvester_uio.py que permite extraer 
#todos los tweets que conforman una vista e imprimirlos a un archivo txt
#Colocar las credenciales de desarrollador de Twitter
#Colocar el nombre correspondiente a la base de datos

import couchdb
import sys
import urllib2

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# encoding:utf-8
##########API CREDENTIALS ############
ckey = ""
csecret = ""
atoken = ""
asecret = ""

URL = 'localhost'
#Colocar nombre de base de datos
db_name = 'new_database'
'''========couchdb'=========='''
server = couchdb.Server('http://' + URL + ':5984/')

try:
    print db_name
    db = server[db_name]
    print "exito"

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

#EJEMPLO DE URL: url = 'http://localhost:5984/new_database/_design/1/_view/tweets1'
url = ''
req = urllib2.Request(url)
f = urllib2.urlopen(req)
sys.stdout=open("tweets.txt","w")
for x in f:
    print(x)
sys.stdout.close()
f.close()
