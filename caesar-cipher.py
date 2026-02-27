# Una función recibe parametros o variables para realizar una tarea específica

# Creamos una función llamada suma
def suma(numero1, numero2):
    # Guardamos en la variable resultado el valor de la suma:
    resultado = numero1 + numero2;
    
    # Devolvemos el valor del proceso
    return resultado
    
# Creamos una variable "a" con lo que diga el usuario:
a = input("Escribe un numero: ")

# Convertirmos la variable a un numero 
a = int(a)

# Creamos una variable "b" con lo que diga el usuario:
b = input("Escribe un numero: ")

# Convertirmos la variable a un numero 
b = int(a)

# LLamamos a la función suma para obtener el resultado y lo imprimimos
print(suma(a, b))


# ------------------------ LABORATORIO -------------------------------

# La idea es “mover” cada letra del mensaje un número de posiciones (la clave).
# Por ejemplo, si la clave es 3: A -> D, B -> E, C -> F, etc.

# Esta función recibe un alfabeto (un texto) y lo pega consigo mismo.
# Lo hacemos para poder “movernos” hacia adelante sin quedarnos sin letras.
# Ejemplo: "ABC" se vuelve "ABCABC".
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
# Esta función le pide al usuario que escriba un mensaje.
# Lo que el usuario escriba se guarda y luego se devuelve.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
# Esta función le pide al usuario una clave.
# La clave es un número del 1 al 25 que indica cuánto se moverán las letras.
def getCiphersKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Esta función hace el trabajo de encriptar.
# Recorre el mensaje letra por letra, busca cada letra en el alfabeto,
# le suma la clave para “moverla”, y va armando el mensaje encriptado.

def runCeasarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alphabet : {alphabet}, size : {len(alphabet)}")
    
    # Duplico el alfabeto para poder desplazar letras sin problemas
    alphabet2 = getDoubleAlphabet(alphabet)
    print(f'Alphabet2: {alphabet2}')
    
    # Pido el mensaje al usuario
    myMessage = getMessage()
    print(myMessage)
    
    # Pido la clave al usuario
    myCipherKey = getCiphersKey()
    print(myCipherKey)
    
    # Encripto el mensaje
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, alphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # Desencripto el mensaje (para comprobar que vuelve al original)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, alphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
# Función encriptación:
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() # Convertimos el texto del mensaje a mayusculas
    
    # Aquí reviso cada letra del mensaje (ya en mayúsculas)
    for currentCharacter in uppercaseMessage:
        # Si la letra llegará a estar en el alfabeto, cambiala por la letra "movida"
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        
        if currentCharacter in alphabet:
            # Busco en que posición está la letra correspondiente:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            # Si no es letra, lo añado como tal
            encryptedMessage = encryptedMessage + currentCharacter
            
    # Al final, devuelvo el texto encriptado completo:
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey);
    
    return encryptMessage(message, decryptKey, alphabet)

# LLamamos la función para poder ejecutarlo en el programa principal:
runCeasarCipherProgram()