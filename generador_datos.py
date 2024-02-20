import json
import random
import threading
import time
import os

def generate_casa_data():
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

def generate_ciudad_data():
    # Generar datos ficticios para una ciudad
    data = {
        "timestamp": int(time.time()),
        "city": {
            "name": random.choice(ciudades),
            "population": random.randint(poblacion_minima, poblacion_maxima),
            "country": "España"
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
        
    # Escribir los datos en el archivo casas.json
    with open(os.path.join(data_folder, "casas_data.json"), "a") as file:
        datos = generate_casa_data() +"\n"
        print(datos)
        file.write(datos)
    # Escribir los datos en el archivo city_data.json
    with open(os.path.join(data_folder, "ciudades_data.json"), "a") as file:
        data = generate_ciudad_data()
        print(data)
        file.write(data + '\n')



espera = 5
ciudades = [
    "Madrid",
    "Barcelona",
    "Valencia",
    "Sevilla",
    "Zaragoza",
    "Málaga",
    "Murcia",
    "Palma de Mallorca",
    "Las Palmas de Gran Canaria",
    "Bilbao",
    "Alicante",
    "Córdoba",
    "Valladolid",
    "Vigo",
    "Gijón",
    "L'Hospitalet de Llobregat",
    "Vitoria-Gasteiz",
    "La Coruña",
    "Granada",
    "Elche",
    "Oviedo",
    "Santa Cruz de Tenerife",
    "Pamplona",
    "Cartagena",
    "Sabadell",
    "Jerez de la Frontera",
    "Móstoles",
    "Alcalá de Henares",
    "Fuenlabrada",
    "Almería",
    "Terrassa",
    "Badalona",
    "Getafe",
    "Donostia-San Sebastián",
    "Leganes",
    "Santander",
    "Burgos",
    "Salamanca",
    "Alcorcón",
    "Albacete",
    "Castellón de la Plana",
    "Logroño",
    "Badajoz",
    "Huelva",
    "Marbella",
    "León",
    "Tarragona",
    "Cádiz",
    "Lleida",
    "Jaén",
    "Ourense",
    "Mataró",
    "Algeciras",
    "Alcobendas",
    "Cáceres",
    "Reus",
    "Telde",
    "Torrejón de Ardoz",
    "Barakaldo",
    "Parla",
    "Santiago de Compostela",
    "San Fernando",
    "Lugo",
    "Girona",
    "Coslada",
    "Talavera de la Reina",
    "Cornellà de Llobregat",
    "El Puerto de Santa María",
    "Melilla",
    "Orihuela",
    "Pontevedra",
    "Pozuelo de Alarcón",
    "Roquetas de Mar",
    "Chiclana de la Frontera",
    "Torrent",
    "San Sebastián de los Reyes",
    "Rubí",
    "Benidorm",
    "Fuengirola",
    "Ciudad Real",
    "Las Rozas de Madrid",
    "Benalmádena",
    "Sanlúcar de Barrameda",
    "Vélez-Málaga",
    "Torrevieja",
    "Zamora",
    "Rivas-Vaciamadrid",
    "Vilanova i la Geltrú",
    "Torrelavega",
    "Línea de la Concepción",
    "Gandia",
    "Manresa",
    "San Vicente del Raspeig",
    "Santa Lucía de Tirajana",
    "Mijas",
    "Majadahonda",
    "Sagunto",
    "Paterna",
    "San Sebastián de La Gomera",
    "Viladecans",
    "Torremolinos",
    "Estepona",
    "Rubí",
    "Molina de Segura",
    "Torrelodones",
    "Elda",
    "Ponferrada",
    "Alcobendas",
    "Arrecife",
    "Cuenca",
    "Valdemoro",
    "Pinto",
    "Sant Cugat del Vallès",
    "Palencia",
    "Alcantarilla",
    "Linares",
    "San Bartolomé de Tirajana",
    "Roquetas de Mar",
    "Coslada",
    "Tudela",
    "El Prat de Llobregat",
    "San Juan de Alicante",
    "Vinaròs",
    "Coslada",
    "Segovia",
    "Cártama",
    "Avilés",
    "Aranda de Duero",
    "Zarautz",
    "Vic",
    "Oliva",
    "Sestao",
    "Irun",
    "Ávila",
    "Parets del Vallès",
    "Paterna",
    "Alzira",
    "Benicarló",
    "Carballo",
    "Vila-real",
    "Sant Adrià de Besòs",
    "Villanueva y Geltrú",
    "Narón",
    "Camargo",
    "Puerto del Rosario",
    "El Ejido",
    "Arona",
    "Manacor",
    "Pineda de Mar",
    "Xàtiva",
    "Mogán",
    "Maó",
    "Los Realejos",
    "Vélez-Málaga",
    "Villaquilambre",
    "El Masnou",
    "La Orotava",
    "Ripollet",
    "Santurtzi",
    "Mazarrón",
    "Begur",
    "Benavente",
    "Leganés",
    "Castro-Urdiales",
    "Caldes de Montbui",
    "Tàrrega",
    "La Oliva",
    "Mijas",
    "Sant Andreu de la Barca",
    "Portugalete",
    "Molina de Aragón",
    "Adra"
  ]

poblacion_minima = 100000
poblacion_maxima = 3000000

generate_and_write_data()
