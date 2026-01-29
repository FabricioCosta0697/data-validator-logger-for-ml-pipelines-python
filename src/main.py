from reader import read_csv

def main():
    try:
        data = read_csv("data/raw_data.csv")
        print(f"{len(data)} registros carregados com sucesso.")
    except Exception as e:
        print(f"Erro na execução: {e}")

if __name__ == "__main__":
    main()
