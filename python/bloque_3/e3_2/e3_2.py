"""
E3.2 · Carga iris.csv con DictReader, convierte las medidas a float
y calcula la media por clase.
"""

import csv 
from pathlib import Path

RUTA = Path(__file__).parent / "iris.csv"

MEDIDAS = ["largo_sep", "ancho_sep", "largo_pet", "ancho_pet"]

def obtener_media_columna(filas, columna):
    """
    Calcula la media de una columna específica agrupando los datos por clase.
    """
    valores = {}
    
    # 1. Agrupamos los valores de la columna según la clase de la flor
    for fila in filas:
        clase = fila["clase"]
        
        # Si la clase aún no está en el diccionario, inicializamos una lista vacía
        if clase not in valores:
            valores[clase] = []
            
        # Añadimos el valor de la columna a la lista correspondiente de esa clase
        valores[clase].append(fila[columna])
    
    resultados = {}
    
    # 2. Calculamos la media (suma total dividida entre la cantidad de elementos) para cada clase
    for clase, v in valores.items():    
        resultados[clase] = sum(v) / len(v)

    # Mostramos los resultados obtenidos
    print(f"Media de '{columna}' por clase:")
    print(resultados)

# --- FLUJO PRINCIPAL ---

# 1. Abrimos el archivo CSV y cargamos su contenido como una lista de diccionarios
with open(RUTA, newline="", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

# 2. Recorremos cada fila para convertir las medidas de texto (str) a números decimales (float)
for fila in filas:
    for m in MEDIDAS:
        fila[m] = float(fila[m])

# 3. Una vez que todas las filas están listas y convertidas, 
# llamamos a la función para calcular y mostrar las medias.

for m in MEDIDAS:
    obtener_media_columna(filas, m)