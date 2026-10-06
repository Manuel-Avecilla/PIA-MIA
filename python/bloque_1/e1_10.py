"""
E1.10 · Tabla de -20 °C a 40 °C de 5 en 5 con su equivalente en
Fahrenheit, en dos columnas alineadas.
"""

MIN = -20
MAX = 40

print(f"| {"Celsius":<7} | {"Fahrenheit":>7} |")
for c in range(MIN,MAX+1,5):
    f = c * 9/5 + 32
    print(f"| {c:<7}°C | {f:>7} F |")