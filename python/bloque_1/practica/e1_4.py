"""
E1.4 · FizzBuzz del 1 al 100, en 6 líneas o menos.

FizzBuzz es un ejercicio clásico de programación para practicar bucles y condicionales del 1 al 100.

Consiste en recorrer cada número e imprimir un resultado según sus divisores:

• Si el número es múltiplo de 3, se muestra "Fizz".
• Si es múltiplo de 5, se muestra "Buzz".
• Si es múltiplo de ambos (3 y 5), se muestra "FizzBuzz".
• En cualquier otro caso, se muestra el número original.

"""

n = int(input("Numero: "))
if(n%3==0 and n%5==0):  t = "FizzBuzz"
elif(n%3==0):           t = "Fizz"
elif(n%5==0):           t = "Buzz"
else:                   t = "" + str(n)
print(t)

"""
# Primer intento

if (n%3 == 0) and (n%5==0):
    print("FizzBuzz")
elif (n%3== 0):
    print("Fizz")
elif (n%5==0):
    print("Buzz")
else:
    print(n)
    
"""