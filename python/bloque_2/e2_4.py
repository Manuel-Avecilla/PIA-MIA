"""
E2.4 · Frecuencia de palabras de un texto: normaliza, separa y
cuenta; muestra el top 5.
"""

SIGNOS = ".,:;!?¡¿()\"'"

def contar_palabras(texto: str) -> dict[str, int]:
    limpio = texto.lower()

    for s in SIGNOS:
        limpio = limpio.replace(s, " ") # quitar puntuación
    # antes de separar

    conteo: dict[str, int]={}
 
    xs = texto.split()
    
    for p in xs:
        if p not in conteo: conteo[p] = 1
        else: conteo[p] += 1
    
    return conteo 
    

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

conteo = contar_palabras(texto)

top5 = sorted(conteo, key=conteo.get, reverse=True)[:5]

print("Top 5 palabras frecuentes")
for palabra in top5:
    print(f"{palabra:_<15} {conteo[palabra]}")


