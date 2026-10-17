"""
E1.2 · Clasificador de notas: pide una nota, valida el rango 0-10 y
muestra la calificación.
"""

n = float(input("Nota: "))

if n not in range(0,11):
    print("True")
else:
    print("False")