# SE COLOCAN LAS IMPORTACIONES DE LAS LIBRERIAS PYTHON EN EL INICIO DEL ARCHIVO
import random


# Un ciclo while es un bucle que va a recorrer hasta que no se cumpla la condición

# Se crea la variable numero y se le pide al usuario que escriba el numero 0
numero = input("Escriba el numero 0")

numero = int(numero)

# Se verifica que lo que hay en la variable número sea menor que 10:
while numero < 10:
    # Se incrementa el valor de numero
    numero = numero + 1
    
    # Si numero es menor que 10 se imprime su valor
    print(numero)
    
# --------------------------------------------------------------------------------

# Vamos a construir la tabla de multiplicar de un numero
# Se crea la variable numero y se le pide al usuario que escria el numero 0

numero = input("Escribir el numero 0: ")

# Convertir la variable de str a int
numero = int(numero)

# Multiplicador
multiplicador = 0

# Se verifica lo que hay en la variable numero sea menor que 10
while multiplicador < 10:
    # Se incrementa el valor de multiplicación
    multiplicador = multiplicador + 1
    # Valor de multiplicación
    multiplicacion = numero * multiplicador
    # Si numero es menor que 10 se imprime su valor
    print(f"{numero} * {multiplicador} = {multiplicacion}")


# ------------------------ LABORATORIO ---------------------------------

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# La libreria Random importada ofrece funciones utiles tales como "randint()" que
# permite seleccionar un numero de forma aleatoria, entre un rango de numeros (en ese caso, del 1 al 10)
number = random.randint(1, 10)

# Creación de la variable isGuessRight y guardarlo a un valor booleano (False)
isGuessRight = False

# WHILE -> Una instrucción de ciclo que hace que un conjunto de instrucciones se ejecutan de forma
# repetitiva siempre y cuando se cumpla con la condición especificada:

# Mientras que isGuessRight sea falso (si aun no lo atina), continua el juego
while isGuessRight != True:
    # Recupera la entrada del usuario (numero)
    guess = input("Guess a number between 1 and 10: ")
    
    # Revisa si la entrada del usuario es igual al numero aleatorio
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))