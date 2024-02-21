from elasticsearch import Elasticsearch

# Conectar con Elasticsearch (asegúrate de que Elasticsearch esté en funcionamiento)
es = Elasticsearch(['http://localhost:9200'])

# Datos que deseas enviar a Elasticsearch
datos = {
    "nombre": "Ejemplo",
    "edad": 30,
    "ciudad": "Ejemploville"
}

# Nombre del índice en Elasticsearch
nombre_indice = "mi_indice"

# Enviar los datos a Elasticsearch utilizando la función index
es.index(index=nombre_indice, body=datos)
