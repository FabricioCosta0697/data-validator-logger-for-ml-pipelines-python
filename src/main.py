from reader import read_csv
from validator import validate_rows
from logger import setup_logger
from report import save_valid_rows_csv, save_errors_json

def main(): # Função principal do programa - carrega dados de um arquivo CSV e imprime o número de registros carregados
    logger = setup_logger() # Configura o logger para registrar informações e erros durante a execução do programa

    try:
        rows = read_csv("data/raw_data.csv")
        logger.info(f"Registros lidos: {len(rows)}")

        valid_rows, errors = validate_rows(rows)

        invalid_count = len(set(e.row_index for e in errors))
        logger.info(f"Validos: {len(valid_rows)}")
        logger.info(f"Invalidos: {invalid_count}")

        save_valid_rows_csv(valid_rows, "reports/valid_rows.csv")
        save_errors_json(errors, "reports/errors.json")
        logger.info("Relatorios gerados em /reports")

        if errors:
            # Mostra alguns erros no console/log sem virar uma bíblia
            for e in errors[:20]:
                logger.warning(f"Linha {e.row_index} | {e.field}: {e.message} (valor: {e.raw_value})")

        logger.info("Execucao finalizada com sucesso.")

    except Exception as e:
        logger.exception(f"Erro na execucao: {e}")

if __name__ == "__main__":
    main()

# Por que fiz assim e o que buscamos:

# main só orquestra: regra de ouro. Ele coordena, não faz trabalho pesado, o que deixa o código mais limpo e fácil de manter. Cada função tem uma responsabilidade clara.

# logger.info/warning/exception: níveis diferentes para separar “normal”, “problema tratável” e “erro sério”, o que é crucial pra análise de logs depois. Você pode filtrar por nível e entender rapidamente o que aconteceu.

# logger.exception: registra stack trace — isso é o que salva sua pele quando algo quebra, porque você tem o contexto completo do erro, não só a mensagem.

# limite de 20 erros exibidos: em produção você não despeja 10 mil linhas no console, isso é inútil. Mostrar um sample dos erros mais comuns já dá uma boa ideia do que está acontecendo, sem virar um caos.

# Isso nos ensina “produção de verdade”: previsível, rastreável e auditável, com logs claros e relatórios estruturados. O código é organizado para ser fácil de entender, manter e escalar, o que é essencial em pipelines de dados reais.