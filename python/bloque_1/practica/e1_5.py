"""
E1.5 · Adivina el número: bucle while con intentos limitados y
pistas mayor/menor.
"""
N_INTENTOS = 3
intentos = 0

NUMERO = 7
n_input = 0

while ( n_input != NUMERO and intentos < N_INTENTOS ):
    print()
    n_input = int(input("Numero: "))
    intentos+=1
    
    if (n_input == NUMERO):
        print("\nCorrecto!!")
        break
    else:
        print("Error: el numero no es correcto.")
        if n_input > NUMERO:    print("El Numero es menor")
        else:                   print("El Numero es mayor")
        print(f"{"Intentos:"}{intentos}{"/"}{N_INTENTOS}")

if (n_input != NUMERO):
    print("\nSe supero el numero de intentos...")