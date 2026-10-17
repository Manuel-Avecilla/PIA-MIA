"""
E2.1 · Estadísticas de una lista de notas: media, máximo, mínimo
y cuántas aprobadas, sin usar statistics.
"""

notas = [7.5, 9.0, 4.2, 6.8]

aprobados = []
for n in notas:
    if n > 5:
        aprobados.append(n)

media = sum(notas) / len(notas)
maximo = max(notas)
minimo = min(notas)

print(f"Media: {media:.2f}")
print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")
print(f"Aprobados: {aprobados}")