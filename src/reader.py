import csv
import os

def read_csv(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    data: list[dict] = []

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if not reader.fieldnames:
            raise ValueError("CSV sem cabeçalho (header)")

        for row in reader:
            data.append(row)

    if not data:
        raise ValueError("CSV vazio: nenhum registro encontrado")

    return data

# Por que fiz assim e o que buscamos:
# Erros explícitos: facilita debug e auditoria, e evita que o pipeline “falhe silenciosamente” ou com mensagens crípticas;
# Header obrigatório: sem schema, tudo vira “cada linha é um universo”, e erros de formatação ficam mais difíceis de detectar;
# CSV vazio: pipeline deve falhar com mensagem útil, não “passar silenciosamente” e gerar relatórios vazios ou incompletos.
