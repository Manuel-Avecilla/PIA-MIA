"""
E1.9 · Con range: múltiplos de 7 hasta 100, cuenta atrás de 10 a 0
y suma de los pares hasta 1000.
"""

t_1 = ""

for n in range(7,101,7):
    t_1 = t_1 + f"{n:>3}"

t_2 = ""

for n in range(10,-1,-1):
    t_2 = t_2 + f"{n:>3}"

t_3 = 0

for n in range(2,1001,2):
    t_3 = t_3 + n

print("\nMúltiplos de 7 hasta 100:")
print(t_1)

print("\nCuenta atrás de 10 a 0:")
print(t_2)

print("\nSuma de los pares hasta 1000:")
print(t_3)