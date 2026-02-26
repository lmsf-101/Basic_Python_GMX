# Se importa la librería "re" para trabajar con expresiones regulares
import re

# Abrimos el archivo de texto:

with open("preproinsulin-seq.txt", "r") as preproinsulin:
    
    raw_data = preproinsulin.read()
    
    # Eliminar el terminador de registro //
    clean_data = re.sub(r"(//)|(1)|(6)|(\bORIGIN\b)|(\n)", "", raw_data)
   #clean_data = re.sub(r"\s", "", clean_data)
    
    # Eliminar los espaciados en blanco
    clean_data = clean_data.strip()
    
    
    with open("preproinsulin-seq-clean.txt", "w") as seq_clean_file:
        seq_clean_file.write(clean_data)
        print("preproinsulin-seq-clean.txt = ", len(clean_data))
        
    with open("lsinsulin-seq-clean.txt", "w") as lsinsulin_file:
        lsinsulin_file.write(clean_data[:24])
        print("lsinsulin-seq-clean.txt = ", len(clean_data[:24]))
        
    with open("binsulin-seq-clean.txt", "w") as binsulin_file:
        binsulin_file.write(clean_data[25:55])
        print("binsulin-seq-clean.txt = ", len(clean_data[25:55]))
        
    with open("cinsulin-seq-clean.txt", "w") as cinsulin_file:
        cinsulin_file.write(clean_data[55:91])
        print("cinsulin-seq-clean.txt = ", len(clean_data[55:90]))
        
    with open("ainsulin-seq-clean.txt", "w") as ainsulin_file:
        ainsulin_file.write(clean_data[90:])
        print("ainsulin-seq-clean.txt = ", len(clean_data[90:]))