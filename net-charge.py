# Voy a guardar las secuencias de insulina como texto (strings).
# Cada letra representa un aminoácido.

# Guardo la secuencia completa de la preproinsulina humana en una variable.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Guardo las partes principales de la insulina en variables separadas.
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# Junto la cadena B y la cadena A para formar la insulina final.
insulin = bInsulin + aInsulin

# Aquí creo un diccionario (como una tablita) con valores pKR.
# La idea es que cada letra tiene un número asociado.
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# Aquí cuento cuántas veces aparecen y, c, k, h, r, d, e dentro de la insulina.
# Lo guardo en un diccionario llamado seqCount.
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}

# Voy a probar distintos valores de pH desde 0 hasta 14 y calcular la carga neta.
pH = 0

while (pH <= 14):
    # Esta es la fórmula que nos dieron para calcular la carga neta.
    # Está dentro del while porque se recalcula en cada pH.
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    
    # Imprimo el pH con 2 decimales y luego la carga neta calculada.
    print('{0:.2f}'.format(pH), netCharge)
    
    # Aumento el pH en 1 para la siguiente vuelta del ciclo.
    pH += 1