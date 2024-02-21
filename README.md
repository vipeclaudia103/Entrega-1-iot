# Entrega 1 - IoT

Repositorio para la entrega de la primera práctica en la asignatura de Desarrollo de Aplicaciones IoT.

- Miembro del equipo: Claudia Viñals Perlado

- Explicación de los pasos seguidos:
    1. Elegir las versiones de Elasticsearch y Filebeat.
    2. Crear el archivo docker-compose con Elasticsearch, Filebeat y Python.
    3. Ejecutar docker-compose y descargar las imágenes.
    4. Programar el código para generar los datos y crear la carpeta donde se almacenarán los archivos JSON.
    5. Crear el archivo filebeat.yml con las configuraciones adecuadas.

- Instrucciones de uso:
    1. Instalación del Docker Compose yendo a la carpeta donde se encuentra el docker-compose.yml. Para ello, utilizar este comando: `docker-compose up -d`
        - Comprobar si están en ejecución los dockers con `docker ps -a` y para saber si Elasticsearch está bien configurado, hacer una consulta tipo GET a `localhost:9200`.
    2. Una vez los contenedores de Elasticsearch y Filebeats están arrancados, ejecutar el docker:
        ```
        sudo docker build -t entrega1 Entrega-1-iot/dockerfile
        sudo docker run --rm entrega1
        ```
    3. Comprobar que los archivos JSON funcionan y crecen cuando se ejecutan abriendo la carpeta de data.
    4. Hacer una consulta GET a `localhost:9200/_cat/indices?v` para comprobar que los índices se han creado.
    5. Hacer una consulta a los índices creados casas y ciudades. Escribir la consulta para ver los datos en el formato:
        - http://localhost:9200/casas/_search
        - http://localhost:9200/ciudades/_search

    ** En el caso de que los índices no se generen por medio del Filebeat, ejecutar el script de 'generador_datos_indices.py', ya que este genera tanto los datos, como crea los índices y envía los datos. Para comprobar su funcionamiento realizar los mismos pasos. 
    
- Posibles vías de mejora:
    - Solucionar la incidencia generada por TLS en la conexión entre Elasticsearch y Filebeat.
    - Incrementar la integración entre los sistemas.

- Problemas / Retos encontrados:
    - Dificultad al crear los índices mediante el archivo filebeat.yml.
        - ** Solución: Realizar el envío desde Python mediante una librería de Elasticsearch.
    - Dificultad en la comprensión de los comandos.

- Alternativas posibles:
    - En lugar de utilizar Python como generador de datos, emplear una API REST desde la cual se tomen los datos.
    - Utilizar Node-RED para interactuar con los contenedores y para el envío y configuración de datos.
    - Utilizar Kubernetes en lugar de Docker Compose para la orquestación de los contenedores.