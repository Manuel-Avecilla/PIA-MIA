"""
E1.6 · Sucesión de Fibonacci hasta N usando asignación múltiple
a, b = b, a + b.
"""

N = 100
a=1
b=2
t = "1"

while b < N:
    t = t + f"{b:>3}"
    a, b = b, a + b

print(t)