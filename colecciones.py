# Para la creación de una lista, se usan corchetes []
# Creación de la lista de myFirstList y unos elementos:
myFruitList = ["apple", "banana", "cherry"]

# Impresion de la lista de frutas completa
print(myFruitList)

# Impresion del tipo de dato que es myFruitList
print(type(myFruitList))

# Impresion de los elementos individuales de la lista myFruitList
print(myFruitList[0]) # apple
print(myFruitList[1]) # banana
print(myFruitList[2]) # cherry

# Modificacion de un elemento particular de la lista (cherry -> orange)
myFruitList[2] = "orange"

print(myFruitList)

# TUPLAS

# Para la creación de una tupla, se usan parentesis ()
# Tuplas sirven para crear un grupo de elementos fijos
# Es decir, una vez creada, no se pueden modificar sus elementos

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acceso de cada elemento de la tupla, esto mediante corchetes []
# Independientemente de si sea lista o tupla, el acceso de elementos se hacen mediante []

print(myFinalAnswerTuple[0]) # apple
print(myFinalAnswerTuple[1]) # banana
print(myFinalAnswerTuple[2]) # pineapple

# DICCIONARIO
# Es un tipo de dato de colección se utiliza pares "llave-valor" para la identificación
# y almacenamiento de los datos

# Se crea mediante el uso de llaves {}

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

# NOTA: Las llaves deben ser UNICAS para el diccionario. Los valores se pueden repetir.
print()
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Para el acceso de un elemento, en lugar de solamente usar el indice numerico,
# se debe especificar la "llave" para poder recuperarlo

# En este caso, para acceder a los valores de "apple", "banana" y "pineapple",
# Es necesario especificar las llaves de "Akua", "Saanvi" y "Paulo", respectivamente

# Al igual que las listas y tuplas, el acceso se realiza mediante corchetes []:

print(myFavoriteFruitDictionary["Akua"]) # apple
print(myFavoriteFruitDictionary["Saanvi"]) # banana
print(myFavoriteFruitDictionary["Paulo"]) # pineapple
