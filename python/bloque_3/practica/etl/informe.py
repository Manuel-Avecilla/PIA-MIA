import csv
import json
from pathlib import Path

def crear_informe(datos, nombre_archivo, extension):
    archivo = nombre_archivo + extension
    ruta = Path(__file__).parent / "informes" / archivo

    match extension:
        case ".json":
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            print(f"Informe guardado en: {ruta}")

        case ".csv":
            if not datos:
                print("No hay datos para escribir en CSV.")
                return

            campos = list(datos[0].keys())
            with open(ruta, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(datos)
            print(f"Informe guardado en: {ruta}")

        case _:
            raise ValueError(f"Extensión '{extension}' no soportada. Usa '.csv' o '.json'.")
