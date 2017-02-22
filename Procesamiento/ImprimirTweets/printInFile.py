import couchdb
import sys
import urllib2

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# encoding:utf-8
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "ZYF88A12e7LeuXJTAM3yEKNAf"
csecret = "MKAXjIjXVWOzpA7PPFdi69iWzSOpRPHSlx9jdlO1IqddFjmZd5"
atoken = "121881131-Xyc6cGon0YSCEgKtaqXxiPIi6C1HYxd2sQOFXkoV"
asecret = "kmDZXdTlwPQKjsJ7HjIqFVgJgfJlTUJlSZdPwsCTLaVkC"

URL = 'localhost'
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

'''===============LOCATIONS=============='''
url = 'http://localhost:5984/new_database/_design/1/_view/esteban1'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
sys.stdout=open("tweetsUIO.txt","w")
for x in f:
    print(x)
sys.stdout.close()
f.close()