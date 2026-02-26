# La libreria CSV nos permite trabajar con archivos separados por coma
import csv

# La libreria "copy" nos permite tomar datos de un archivo y usarlos dentro de un programa
import copy

# Creación del diccionario myVehicle que funcionará como tipo compuesto para leer datos tabulares
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Se crea un ciclo for para imprimir cada una de los pares clave-valor que se encuentran en el diccionario
for key, value in myVehicle.items():
    # Se imprime el par clave-valor
    print("{} : {}".format(key,value))

# Se crea la lista myInventoryList

myInventoryList = []


# COPIA DEL ARCHIVO CSV EN MEMORIA

# Se abre el archivo car_fleet.csv en modo lectura, la cual es guardada en una variable temporal
# denominada "csvFile":
with open('car_fleet.csv') as csvFile:
    # Se lee el archivo almacenado en csvFile, especificando que el delimitador son las comas:
    csvReader = csv.reader(csvFile, delimiter=',')  
    
    # Se genera una variable lineCount con valor de 0
    lineCount = 0  
    
    # Se LEE cada una de las lineas dentro de csvReader:
    for row in csvReader:
        # Si el valor de las lineas es 0 (es decir, es el encabezado)
        if lineCount == 0:
            # Se imprime el nombre de las columnas
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        
        # Si el valor de la linea no es igual a 0:
        else:
            # Imprime en cada una de las claves la posición que fue separada por coma, anteriormente:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # Se copia el valor de las variables dentro del diccionario myVehicle
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            # Se agrega a la lista de vehiculos
            myInventoryList.append(currentVehicle)  
            
            # Se le aumenta lineCount a 1
            lineCount += 1  
            
    # Se imprime el numero total de lineas procesadas
    print(f'Processed {lineCount} lines.')
    
# Se crea un ciclo for para imprimir cada vehículo de la lista:
for myCarProperties in myInventoryList:
    
    # Se imprimen los datos de cada vehículo
    for key, value in myCarProperties.items():
        # Se imprime el par de llave-valor
        print("{} : {}".format(key,value))
        print("-----")
