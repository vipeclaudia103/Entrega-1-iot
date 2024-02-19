import json
import random
import threading
import time
import os

def generate_dummy_data():
    # Generar datos ficticios para una casa
    data = {
        "timestamp": int(time.time()),
        "house": {
            "rooms": random.randint(1, 10),
            "bathrooms": random.randint(1, 5),
            "size_sqft": random.randint(500, 5000),
            "year_built": random.randint(1900, 2022),
            "price_usd": random.randint(100000, 1000000)
        }
    }
    return json.dumps(data)

def generate_and_write_data():
    global espera
    t = threading.Timer(espera, generate_and_write_data)
    t.start()
    
    # Crear el directorio de datos si no existe
    data_folder = "/home/cvp/repos/Entrega-1-iot/data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        
    # Escribir los datos en el archivo dummy_data.json
    with open(os.path.join(data_folder, "dummy_data.json"), "a") as file:
        datos = generate_dummy_data()
        print(datos)
        file.write(datos)

espera = 5
generate_and_write_data()
