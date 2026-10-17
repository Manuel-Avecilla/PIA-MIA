"""
E1.8 · Ticket de compra: nombre alineado a la izquierda,
unidades centradas y precio a la derecha con 2 decimales.
"""

# E1.8 esqueleto

compra = [  ("Teclado", 1, 24.9),
            ("Raton", 2, 12.5),
            ("Monitor", 1, 189.0)]

for nombre, uds, precio in compra:
    print(f"{nombre:<12}{uds:^6}{precio:>10.2f}")

# Teclado 1 24.90