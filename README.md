# proyecto-2do-Bimestre-BI
DISEÑO E IMPLEMENTACIÓN DE UN SISTEMA CLASIFICADOS DE SENTIMIENTOS PARA POLITICA

COLABORADORES:
              
Díaz Esteban            
Muñoz Richard

Tapia Armando
              
DESCRIPCIÓN:

Durante el proyecto se trabajó con las herramientas CouchDB, ElasticSearch, Logstash, Kibana y Pycharm.

CouchDB se utilizó para almacenar y filtrar los tweets.  

Pycharm es un IDE que soporta lenguajes XML, HTML, XHTML y Python.
Este último se utilizó para escribir los scripts que automatizaron la limpieza y el análisis de los tweets.


Logstash: Es un pipeline de procesamiento de datos que recoge los mismos de múltiples fuentes.

Elasticsearch: Permite hacer busqueda sobre texto y realizar análisis de sentimientos.

Kibana: Permite visualizar los datos de Elasticsearch. Presenta la información usando gráficos de barras, líneas, mapas o pasteles.

River: Plugin para ElasticSearch que permite indexar los documentos de couchdb para poder visualizarlos en ElasticSearch.



INSTRUCCIONES DE INSTALACIÓN Y FUNCIONAMIENTO


<br>REQUISITOS PREVIOS PARA EL FUNCIONAMIENTO DEL PROYECTO

Tutorial para instalar CouchDB versión 1.6.1: https://www.digitalocean.com/community/tutorials/how-to-install-couchdb-and-futon-on-ubuntu-14-04

INSTALACION COUCHDB

Pasos de Instalacion 
 
sudo apt-get update
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:couchdb/stable -y


Instalacion 
sudo apt-get remove couchdb couchdb-bin couchdb-common -yf
sudo apt-get install couchdb -y
curl localhost:5984


Creacion de la BD
curl -X PUT localhost:5984/new_database

Tutorial para instalar Pycharm Community 2016 versión 3.2 :https://www.jetbrains.com/pycharm/download/#section=linux


INSTALACION PYCHARM


Instalación PyCharm en Linux


Descargar el zip:
<pycharm-professional or pycharm-community>-*.tar.gz

Descomprimirlo:
tar xfz <pycharm-professional or pycharm-community>-*.tar.gz <new_archive_folder>

Cambiar al directorio /bin:
cd <new archive folder>/<pycharm-professional or pycharm-community>-*/bin

Ejecutar pycharm.sh desde el directorio /bin


Tutorial para instalar Elasticsearch, Kibana, Logstash, Nginx: https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-ubuntu-14-04


Repositorio de versionamiento del plugin River versión 2.5: https://github.com/elastic/elasticsearch-river-couchdb



INSTALACION ELASTICSEARCH, KIBANA, JAVA8, PLUGIN RIVER

Prerequisitos

- Ubuntu Server 14.04
- RAM: 4GB
- CPU: 2 (Recomendado)

Instalar Java 8

Añadir el repositorio con:
sudo add-apt-repository -y ppa:webupd8team/java

Actualizar base de datos de paquetes e instalar:
sudo apt-get update && install oracle-java8-installer -y

Instalar Elasticsearch

Añadir la clave pública GPG en apt:
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

Crear lista de recursos
echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list

Actualizar base de datos de paquetes e instalar
sudo apt-get update && install elasticsearch -y

Editar el archivo de configuración de elasticsearch
sudo vi /etc/elasticsearch/elasticsearch.yml
Realizar cambios en: network.host: localhost
Reiniciar el servicio:
sudo service elasticsearch restart

Iniciar elasticsearch durante el arranque:
sudo update-rc.d elasticsearch defaults 95 10

Instalar Kibana

Crear lista de recursos:
echo "deb http://packages.elastic.co/kibana/4.4/debian stable main" | sudo tee -a /etc/apt/sources.list.d/kibana-4.4.x.list

Actualizar e instalar:
sudo apt-get update -y install kibana

Editar la configuración de kibana:
sudo vi /opt/kibana/config/kibana.yml
Y reaizar el cambio:
server.host: "localhost"

Configurar para que kibana inicie en el arranque:
update-rc.d kibana defaults 96 9
Y reiniciar el servicio:
sudo service kibana start

Para poder hacer funcionar CouchDB junto con Elasticsearch es necesario
instalar el plugin river.
Cambiar al directorio:
cd /usr/share/elasticsearch/
Instalar el plugin:
./bin/plugin -install elasticsearch/elasticsearch-river-couchdb/1.2.0

Reiniciar el servicio:
service elasticsearch restart

Crear el indice:
curl -X PUT '127.0.0.1:9200/_river/testdb/_meta' -d '{ "type" : "couchdb", "couchdb" : { "host" : "localhost", "port" : 5984, "db" : "testdb", "filter" : null }, "index" : { "index" : "testdb", "type" : "testdb", "bulk_size" : "100", "bulk_timeout" : "10ms" } }'
Probar en elasticsearch:
curl http://127.0.0.1:9200/testdb/testdb/_search?pretty=true






Una vez instaladas todas estas herramientas, se procede a seguir las fases del proyecto en orden secuencial.

Primera fase del proyecto:
<p>La recoleccion o adquisicion de datos a traves del script harvester_uio.py ubicado en la carpeta "1 Adquisicion"
El script en python se ejecuta en linea de comandos con la siguiente estructura:
python harvester_uio.py localhost "nombre de base de datos"</p>

Segunda fase del proyecto:
<p>Si se utilizan dos maquinas para la recoleccion de datos es necesario centralizar la informacion.
Para transportar la informacion entre dos maquinas se debe seguir los siguientes pasos:</p>
<p>1. Ingresar al directorio /etc/couchdb (como superusuario) que contiene los archivos de configuración del couchdb para permitir el acceso remoto.
			comando: cd /etc/couchdb/</p>
<p>2. Editar como superusuario el archivo de configuracion default.ini dentro de la carpeta couchdb.
En la sección [httpd] comentar la línea bind_adddress con punto y coma (;) y agregar una nueva línea:
			bind_adddress = 0.0.0.0</p>
<p>3. Guardar los cambios y reinicar el servicio de couchdb.
		sudo service couchdb restart</p>
<p>4. Replicar desde la maquina principal que va a contener todos los tweets con el comando:</p>
		


Tercera fase del proyecto:
<p>Crear dos proyectos en Pycharm con los siguientes componentes:</p>
<p>1.	Proyecto “ImprimirTweets”
	Contiene un archivo llamado printInFile.py</p>
<p>2.	Proyecto “ProcesarTweets”
	Contiene dos archivos llamado openFile.py y deleteSpecials.py</p>

<p>Para que el procesamiento sea correcto se debe seguir el siguiente orden de ejecución:</p>
<p>1.	Ejecutar archivo printInFile.py de la carpeta ImprimirTweets.
	Se genera el archivo tweetsUIO.txt</p>
<p>2.	Ejecutar archivo openFile.py de la carpeta ProcesarTweets.
Se genera el archivo tweetValue.txt</p>
<p>3.	Ejecutar archivo deleteSpecials.py de la carpeta ProcesarTweets.
	Se genera el archivo processedTweets.txt</p>


Cuarta fase del proyecto:
<p>configurar indice en elasticSearch e ingresar a la url: localhost:9200/_plugin/head para revisar los tweets indexados</p>


Quinta fase del proyecto:
Realizar la presentacion de los datos mediante Kibana




