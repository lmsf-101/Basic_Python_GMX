# Guardar la secuencia completa de preproinsulina:

preProinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = "malwmrllpllallalwgpdpaaa" 
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt" 
aInsulin = "giveqcctsicslyqlenycn" 
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Aquí junto la cadena B y la cadena A.
# El símbolo + sirve para pegar textos.
insulin = bInsulin + aInsulin

# Ahora voy a imprimir cosas en pantalla.

# Imprimo un mensaje primero, sobre la secuencia de preproinsulina.
print("La secuencia de la preproinsulina humana es:", preProinsulin)

# Aquí imprimo texto y le agrego la cadena A.
print("La secuencia de la insulina humana, cadenaA: " + aInsulin);

# Aquí creo un diccionario.
# Es como una tabla donde cada letra tiene un peso.
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}


# Aquí cuento cuántas veces aparece cada letra en la insulina.
# upper() convierte todo a mayúsculas.
# count(x) cuenta cuántas veces aparece la letra.
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}

# Aquí multiplico la cantidad de cada aminoácido por su peso.
# Después sumo todos los resultados.
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

# Muestro el peso molecular aproximado.
# Uso str() porque no puedo juntar texto con número directamente.
print("El peso molecular aproximado de la insulina es: " +
str(molecularWeightInsulin))

# Aquí guardo el valor real del peso molecular.
molecularWeightInsulinActual = 5807.63

# Aquí calculo el porcentaje de error.
# Fórmula: ((calculado - real) / real) * 100
print("Porcentaje de error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))