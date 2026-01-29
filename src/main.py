from reader import read_csv
from validator import validate_rows

def main(): # Função principal do programa - carrega dados de um arquivo CSV e imprime o número de registros carregados
    try: # sem uso de try/except genérico, apenas para capturar erros específicos
        rows = read_csv("data/raw_data.csv")
        valid_rows, errors = validate_rows(rows)

        print(f"Registros lidos: {len(rows)}")
        print(f"Válidos: {len(valid_rows)}")
        print(f"Inválidos: {len(set(e.row_index for e in errors))}")

        if errors:
            print("\nErros encontrados:")
            for e in errors[:20]:  # limita pra não virar um livro
                print(f"- Linha {e.row_index} | {e.field}: {e.message} (valor: {e.raw_value})")

    except Exception as e:
        print(f"Erro na execução: {e}")

if __name__ == "__main__":
    main()
