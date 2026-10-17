"""
E1.1 · Conversor de unidades: pide grados Celsius y muestra
Fahrenheit y Kelvin con 2 decimales.
"""

c = float(input("Grados Celsius: "))

f = c * 9/5 + 32

k = c + 273.15

print(f"{c:.2f} C = {f:.2f} F")

print(f"{c:.2f} C = {k:.2f} K")