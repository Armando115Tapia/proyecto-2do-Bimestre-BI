
#Código compartido por la Ing. Elisa Mena de la Facultad de Ingeniería 
#de Sistemas de la Escuela Politécnica Nacional
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

##########API CREDENTIALS ############   
#Colocar credenciales del API de dev de Twitter
ckey = ""
csecret = ""
atoken = ""
asecret = ""
 
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
server = couchdb.Server('http://'+URL+':5984/')  #Colocar URL de base de datos
 

try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
twitterStream.filter(locations=[-78.593445,-0.370099,-78.386078,-0.081711])  #Coordenadas QUITO 


#Colocar este archivo en el escritorio de la máquina, ejecutarlo mediante el comando: 
#python harvester_uio.py localhost nombredebasededatos
