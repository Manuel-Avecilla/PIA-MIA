import csv
from pathlib import Path

RUTA = Path(__file__).parent / "ventas_sucio.csv"

def get_filas():
    with open(RUTA, newline="") as f:
        return list(csv.DictReader(f))