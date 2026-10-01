"""
E1.3 · Tabla de multiplicar con formato alineado usando f-strings.
"""

t = int(input("Tabla: "))

for x in range(0,11):
    r = x * t
    print(f"{t:^2} {"x":^2} {x:^2} {"=":^2} {r:^2}")