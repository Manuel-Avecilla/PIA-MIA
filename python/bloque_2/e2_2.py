"""
E2.2 · Deduplicar conservando el orden de aparición original. Es
decir, elimina las copias repetidas de una lista.
"""

# E2.2 esqueleto
notas = {"ana": 7, "leo": 9, "eva": 7}

por_nota = {}

for alumno, nota in notas.items():
    
    if nota not in por_nota.keys():
        por_nota[nota]=[alumno]
    
    else:
        xs = por_nota[nota]
        xs.append(alumno)

print(por_nota)
# {7: ["ana", "eva"], 9: ["leo"]}

