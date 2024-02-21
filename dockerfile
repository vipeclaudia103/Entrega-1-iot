# Usa la imagen base de Python 3.10
FROM python:3.10

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crea una carpeta /app y establécela como el directorio de trabajo
RUN mkdir /app
WORKDIR /app

# Copia el archivo Python creado previamente al directorio de trabajo
COPY generador_datos.py /app

# Comando por defecto para ejecutar cuando se inicie el contenedor
CMD ["python", "generador_datos.py"]
