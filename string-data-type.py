myString = "This is a string"
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

# Concatenación de cadenas
# Se produce mediante el más (+), donde unirá las dos cadenas en una sola
firstStr = "water"
secondStr = "fall"
thirdStr = firstStr + secondStr

print(thirdStr)

# Uso de la funcion input() para obtener una entrada del usuario.
# El código se detendrá hasta que el usuario introduce información
name = input("What is your name? ")

print(name)

# DANDO FORMATO A LAS CADENAS DE SALIDA

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

# Para imprimir usando format() vamos a poner un {} por cada variable 
# y el format() va a poner el valor de las variables en el orden que 
# se estan usando

print("{}, you like a {} {}!".format(name, color, animal))