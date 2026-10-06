"""
E2.3 · Agenda: diccionario de contactos con alta, baja, búsqueda
y listado ordenado, en un bucle de menú.
"""

opcion = 0
contactos = {"ana": 123456789, "leo": 987654321, "eva": 123123123}

t =     f"{"Agenda":-^30}"+"\n"
t +=    f"{"Opcion 1: alta"}"+"\n"
t +=    f"{"Opcion 2: baja"}"+"\n"
t +=    f"{"Opcion 3: búsqueda"}"+"\n"
t +=    f"{"Opcion 4: listado ordenado"}"+"\n"
t +=    f"{"Opcion 5: salir"}"+"\n"
t +=    f"{"-":-^30}"+"\n"
print(t)

while (opcion != 5):
    
    opcion = int(input("Elige una opción: "))
    
    print()
    
    match opcion:
        case 1:
            print(f"{"Opcion 1: alta":-^30}"+"\n")
            print(min(contactos.keys())+"\n")
        
        case 2:
            print(f"{"Opcion 2":-^30}"+"\n")
            print(max(contactos.keys())+"\n")
        
        case 3:
            print(f"{"Opcion 3":-^30}"+"\n")
            continue
        
        case 4:
            print(f"{"Opcion 4":-^30}"+"\n")
            continue
        
        case 5:
            print(f"{"Agenda cerrada":-^30}"+"\n")
            break
        
        case _:
            print("Error: Opcion incorrecta")
            continue
