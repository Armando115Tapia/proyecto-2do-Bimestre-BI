import json
import sys
from pprint import pprint
import urllib2
# encoding:utf-8

valor = '"value":"'

with open('/root/PycharmProjects/ImprimirTweets/tweetsUIO.txt') as f:
    for line in f:
        line.split(valor)
        #print(line.split("value"))
        #result = line.split('value:')[-1]
        result = line.split(valor)[-1]
        #print(result)
        f1=open('/root/PycharmProjects/ProcesarTweets/tweetsValue.txt','a')
        f1.write(result)
        f1.close()