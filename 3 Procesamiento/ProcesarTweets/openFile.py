
#Código escrito en lenguaje python que permite leer el archivo .txt creado por printInFile 
#con el objetivo de extraer el campo value que contiene el texto de cada tweet recolectado

import json
import sys
from pprint import pprint
import urllib2
# encoding:utf-8

valor = '"value":"'

#Ejemplo de directorio Proyecto Pycharm:
#with open('/root/PycharmProjects/ImprimirTweets/tweets.txt') as f:
with open('') as f:
    for line in f:
        line.split(valor)
        #print(line.split("value"))
        #result = line.split('value:')[-1]
        result = line.split(valor)[-1]
        #print(result)
        #Ejemplo de directorio Proyecto Pycharm:
        #f1=open('/root/PycharmProjects/ProcesarTweets/tweetsValue.txt','a')
        f1=open('','a')
        f1.write(result)
        f1.close()
