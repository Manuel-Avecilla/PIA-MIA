"""
E1.7 · Conversor seguro: pide un valor e indica si es entero,
decimal o no numérico, convirtiéndolo al tipo adecuado.
"""

v = 4

if type(v) == int: print("Tipo Entero")
if type(v) == float: print("Tipo Decimal")
if (type(v) != float) and (type(v) != int): print("Tipo No Numerico")

