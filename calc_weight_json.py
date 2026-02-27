# Importar el módulo que creé para leer los archivos JSON:
import jsonFileHandler

# Llamo a la función para leer el archivo JSON
# Le paso la ruta donde está guardado
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Verifico que el archivo se haya leido correctamente:
if data != "":
   # Extraigo la cadena B desde el JSON
   bInsulin = data['molecules']['bInsulin']
   
   # Extraigo la cadena A desde el JSON
   aInsulin = data['molecules']['aInsulin']
   
   # Uno ambas cadenas para formar la insulina completa
   insulin = bInsulin + aInsulin
   
   # Extraigo el peso molecular real desde el JSON
   molecularWeightInsulinActual = data['molecularWeightInsulinActual']
   
   # Impresion de los datos obtenidos:
   print(f"bInsulin: {bInsulin}")
   print(f"aInsulin: {aInsulin}")
   print(f"molecularWeightInsulinActual: {molecularWeightInsulinActual}")
   
   # Obtengo el peso de todos los aminoácidos de los datos JSON:
   aaWeights = data['weights']
   
   aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}

   # Multiplico la cantidad de cada aminoácido por su peso
   # Luego sumo todos los resultados
   molecularWeightInsulin = sum({
      x: (aaCountInsulin[x] * aaWeights[x]) 
      for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
      'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
   }.values())
   
   # Muestro el peso calculado
   print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
   
   # Calculo el porcentaje de error
   # Fórmula: (calculado - real) / real * 100
   percentError = ((molecularWeightInsulin - molecularWeightInsulinActual) /
      molecularWeightInsulinActual) * 100
      
   print("Percent error: " + str(percentError))
else:
   # Si el archivo no se pudo leer, termina el programa
   print("Error. Exiting program")