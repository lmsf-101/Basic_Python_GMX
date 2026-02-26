# Definición de una lista con elementos de diferentes
# tipos de datos
# Python no restringe sobre que tipo de dato se debe
# meter en una lista: Es muy flexible

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Para verificar, se hace uso de un ciclo for (instruccion de ciclo / iteración)
# Donde para cada elemento de la lista, se imprime su valor y tipo de dato:
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))