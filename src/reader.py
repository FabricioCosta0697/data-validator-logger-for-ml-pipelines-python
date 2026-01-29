import csv
import os

def read_csv(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    data = []

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if reader.fieldnames is None:
            raise ValueError("CSV sem cabeçalho")

        for row in reader:
            data.append(row)

    if not data:
        raise ValueError("CSV vazio")

    return data
