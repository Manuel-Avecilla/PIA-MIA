"""
E2.5 · Normaliza una lista de valores al rango 0-1 con una sola
comprensión.
"""

# E2.5 normalización min-max

valores = [12, 7, 30, 18]

lo, hi = min(valores), max(valores)

norm = [(x - lo) / (hi - lo) for x in valores].sort()

print(norm)

# [0.17, 0.0, 1.0, 0.48]

"""

utilizando un bucle tradicional:

norm = []

for x in valores:    
    resultado = (x - lo) / (hi - lo)
    norm.append(resultado)

"""