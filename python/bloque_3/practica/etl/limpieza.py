import re # Para utilizar expresiones regulares

def limpiar(fila):
    """
    Valida y limpia una fila de ventas.
    Si algún campo no cumple con el formato esperado, lanza ValueError
    con un mensaje descriptivo que main.py captura.
    """
    # Si la fila tiene columnas de más o de menos (por ejemplo comas extra en números)
    if None in fila or None in fila.values():
        raise ValueError("Número de columnas incorrecto o campos mal delimitados")

    fila_limpia = {}

    for key, value in fila.items():
        # Aseguramos que el valor sea texto y quitamos espacios sobrantes
        val = str(value).strip() if value is not None else ""

        match key:
            case "fecha":
                # Formato esperado: YYYY-MM-DD
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", val):
                    raise ValueError(f"Fecha inválida: '{val}' (debe ser AAAA-MM-DD)")
                fila_limpia["fecha"] = val

            case "producto":
                # Solo letras (incluyendo tildes/espacios si fuera necesario) y no vacío
                if not re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ]+", val):
                    raise ValueError(f"Producto inválido o vacío: '{val}'")
                fila_limpia["producto"] = val.lower()

            case "unidades":
                # Enteros positivos mayores que 0 (solo dígitos)
                if not re.fullmatch(r"[1-9]\d*", val):
                    raise ValueError(f"Unidades inválidas: '{val}' (debe ser un entero positivo)")
                fila_limpia["unidades"] = int(val)

            case "precio_unitario":
                # Número decimal o entero positivo (ej: 24.90, 189, 3.75)
                if not re.fullmatch(r"\d+(\.\d{1,2})?", val):
                    raise ValueError(f"Precio unitario inválido: '{val}'")
                fila_limpia["precio_unitario"] = float(val)

            case "vendedor":
                # Nombre del vendedor: solo letras y no vacío
                if not re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ]+", val):
                    raise ValueError(f"Vendedor inválido o vacío: '{val}'")
                fila_limpia["vendedor"] = val.lower()

            case _:
                # Cualquier otra columna no contemplada
                fila_limpia[key] = val

    return fila_limpia