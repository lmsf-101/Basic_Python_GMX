# Se va a crear un validador para saber si podemos o no podemos
# entrar a una fiesta. Es importante agregar que para entrar,
# debes ser mayor de edad.
"""
edad = int(input("Escriba su edad "))

# Vamos a comparar si la edad es mayor o igual que 18 años
if edad >= 18:
    # Imprime que lo dejara entrar
    print("Puede entrar")
else:
    # Si no se cumple la condicion de ser mayor-igual de 18 años,
    # Imprimir que no puede entrar
    print("NO PUEDE ENTRAR")
    
# Ahora, se va a validar si la persona es mayor de edad y además
# tiene más de 600 pesos.
edad = input("Escriba su edad ")
edad = int(edad)

dinero = input("Cuanto dinero tienes? ")

dinero = int(dinero)

# Vamos a comparar si la edad es mayor o igual a los 18 años
if edad >= 18:
    # Verificar si tiene dinero suficiente
    if dinero > 600:
        # Imprimir que lo deja entrar
        print("Puedes entrar")
    else:
        print("NO PUEDE ENTRAR: DINERO INSUFICIENTE")
else:
    print("NO PUEDE ENTRAR: ERES MENOR DE EDAD")
    
# Vamos a comparar si la edad es mayor o igual a los 18 años (VERSION #2)
if (edad >= 18) & (dinero >= 600):
    # Imprimir que lo deja entrar
    print("Puedes entrar")
else:
    print("NO PUEDE ENTRAR")

# -------------------------------------------------------------------
# CONDICIONAL CON MULTIPLES COMPARACIONES

# Uso de elif

# Creamos la variable llamada "dinero"
dinero = input("Escriba la cantidad de dinero que cuenta : ")

# Conversion de la entrada en string a un numero entero:
dinero = int(dinero)

if dinero < 100:
    print("Le compro unas galletas :)")
elif dinero >= 100 and dinero <= 200:
    print("Le compro unos chocolates 🍫")
elif dinero > 200 and dinero <= 300:
    print("Le compro unas 300 picafresas")
else:
    print("Le compro un peluche 🧸")
"""
# -----------------------------------------------------------------

# ELABORACIÓN DEL LABORATORIO

# Creación de la variable "userReply" que guardamos la respuesta del usuario:
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Uso de la instrucción "if" para indicar la validación de una condición especifica
# Aqui, la instrucción busca si la respuesta almacenada en "userReply" es EXACTAMENTE igual a "yes"

# Ojo, como se esta trabajando con cadenas en este caso, el uso del operador de igualdad (==), provoca que
# Python revise si el los dos textos son exactamente iguales, tanto en mayusculas como en minusculas (sensible a mayusculas):
if userReply == "yes":
    print("We can help you with that package")

# INSTRUCCIÓN ELSE
# Se usa "else" como la instrucción inversa del "if" que se ejecuta si la condición del "if" resultó falso:
else:
    print("Please come back when you need to ship a package. Thank you.")


# INSTRUCCIÓN ELIF
# Para la creación de estructuras de control más complejas, se tiene la opción de "elif" que
# permite especificar condiciones adicionales, en dado caso que la condición "if" no se haya cumplido

# Pueden ser de 0...N instrucciones elif, que se ejecutan si la condición previa (if u otro elif) resulto falsa:

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Condicion inicial
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
    
# Si el usuario no seleccionó "stamps", revisa si se seleccionó "envelope"
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")

# Si no fue "envelope", revisa "copy"
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
    
# En todo caso, si no cumple con ninguna de las condiciones anteriores, realiza una instrucción "predeterminada"
else:
    print("Thank you, please come again.")