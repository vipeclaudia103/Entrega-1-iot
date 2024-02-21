# Entrega 1 - IoT

Repositorio para la entrega de la primera práctica en la asignatura de Desarrollo de Aplicaciones IoT.

• Miembro del equipo: Claudia Viñals Perlado

• Explicación de los pasos seguidos:
    1. Elegir las versiones de Elasticsearch y Filebeat.
    2. Crear el archivo docker-compose con Elasticsearch, Filebeat y Python.
    3. Ejecutar docker-compose y descargar las imágenes.
    4. Programar el código para generar los datos y crear la carpeta donde se almacenaran los json
    5. Crear el archivo filebeat.yml con las configuraciones adecuadas.


• Instrucciones de uso:
    1. Instalación del Docker Compose yendo a la carpeta donde se encuentra el docker-compose.yml. Para ello, utilizar este comando:
        ```
        docker-compose up -d
        ```
        --> Comprobar la si estan en ejecución los dockers con docker ps -a y para saber si elasticsearch esta bien configurado hacer una consulta tipo get a 'localhost:9200'
    2. Una vez los contenedores de elasticsearch y filebeats estan arrancados ejecutar el docker con el codigo de creación de datos.
    3. Comprobar que los archivos json funcionan y crecen cuando se ejecutan
    4. Hacer una consulta GET localhost:9200/_cat/indices?v para comprobar que los indices se han creado
    5. Hacer una consulta a los indices creados casas y ciudades
• Posibles vías de mejora:
    - Solucionar la indicendia generada por TLS la conexión entre Elasticsearch y Filebeat.
    - Incrementar la integración entre los sistemas.
    - En 

• Problemas / Retos encontrados:
    - Dificultad al crear los índices mediante el archivo filebeat.yml.
        ** Solución: Realizar el envío desde Python mediante una librería de Elasticsearch.
    - Dificultad en la comprensión de los comandos.

• Alternativas posibles:
    - En lugar de utilizar Python como generador de datos, emplear una API REST desde la cual se tomen los datos.
    - Utilizar Node-RED para interactuar con los contenedores y para el envío y configuración de datos.
    - Utilizar Kubernetes en lugar de Docker Compose para la orquestación de los contenedores.