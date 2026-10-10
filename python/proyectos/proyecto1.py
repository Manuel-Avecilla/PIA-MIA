"""

PROYECTO 1 · ENUNCIADO

Analizador de un conjunto de flores

Partes de un dataset embebido en el código como texto
(formato CSV, 30 filas del conjunto Iris).

1 · Parsear el texto a una lista de diccionarios con tipos correctos.

2 · Calcular, por clase: número de muestras, media, mínimo y
máximo de cada medida.

3 · Normalizar las medidas al rango 0-1 con una comprensión.

4 · Detectar y listar los valores atípicos (a más de 2 desviaciones
de la media).

5 · Imprimir un informe alineado con f-strings.

"""

DATOS = """5.1,3.5,1.4,0.2,setosa,4.9,3.0,1.4,0.2,setosa,7.0,3.2,4.7,1.4,versicolor"""

COLUMNAS = ["largo_sep", "ancho_sep","largo_pet", "ancho_pet","clase"]

def parsear(texto):
    """Devuelve lista de dicts."""