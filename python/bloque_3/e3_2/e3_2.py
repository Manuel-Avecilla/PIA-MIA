"""
E3.2 · Carga iris.csv con DictReader, convierte las medidas a float
y calcula la media por clase.
"""

# E3.2

import csv 
from pathlib import Path

RUTA = Path(__file__).parent / "iris.csv"
MEDIDAS = ["largo_sep","ancho_sep","largo_pet","ancho_pet"]

def obtener_media_columna(filas,columna):
    valores={}
    
    for fila in filas:
        clase = fila["clase"]
        
        if clase not in valores:
            valores[clase] = []
            valores[clase].append(fila[columna])
    
    resultados={}
    
    for clase, v in valores.items():    
        resultados[clase] = sum(v)/len(v)

    print(resultados)

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))


for fila in filas:

    # print(fila)
    
    # Conversion
    for m in MEDIDAS:
        fila[m]=float(fila[m])
    
    obtener_media_columna(filas,"largo_sep")
    




