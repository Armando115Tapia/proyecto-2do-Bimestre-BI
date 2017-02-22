
'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
#encoding:utf-8 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "woSkEr2S3SqDEc5LP7d16viE0"
csecret = "D8ENCpcgjNd9CIREnlf49wk9KLescGwUQYVdbiPkv4ZfYJ25YV"
atoken = "775384416902320128-41ZI74CIZ4LDhGlsu3bw2LSYRH3G4cw"
asecret = "8pdxewymMZOgHSJZ4SGv6qFpWOIQzIqHUPxJTvJNBmGUc"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
if len(sys.argv)!=3:
    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
    sys.exit()
 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
# server = couchdb.Server('http://localhost:5984/_utils/document.html?tweets/0cd20a809b94db5eb1f75cef9b0010a8')
 

try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
twitterStream.filter(locations=[-78.593445,-0.370099,-78.386078,-0.081711])  #QUITO 

