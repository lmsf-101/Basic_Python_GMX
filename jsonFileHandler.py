# Importo la librería json que me permite trabajar con archivos JSON
import json

# Creo una función que recibe el nombre del archivo JSON
def readJsonFile(fileName):
    
    # Inicializo la variable data como vacía
    # Si algo falla, devolverá esto:
    data = ""
    
    try:
        # Intento abrir el archivo que me pasaron como parámetro:
        with open(fileName) as json_file:
            # json.load convierte el archivo JSON en un diccionario de Python
            data = json.load(json_file)
            
    except IOError:
        # Si ocurre un error al abrir el archivo, muestro este mensaje
        print("Could not read file")
        
    # Devuelvo los datos leídos (o vacío si falló)
    return data
    
