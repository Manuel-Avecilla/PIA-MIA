"""
E2.6 · Dado un texto, construye {palabra: frecuencia} y devuelve
las 3 más repetidas usando sorted con key.
"""

from e2_4 import contar_palabras

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

conteo = contar_palabras(texto)

top3 = sorted(conteo, key=conteo.get, reverse=True)[:3]

print("Top 3 palabras mas frecuentes")
for palabra in top3:
    print(f"{palabra:<15} {conteo[palabra]}")
