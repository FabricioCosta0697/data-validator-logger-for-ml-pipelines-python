import argparse

from reader import read_csv
from validator import validate_rows
from logger import setup_logger
from report import save_valid_rows_csv, save_errors_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validador de dados para pipelines de ML com logs e relatórios."
    )
    parser.add_argument("-i", "--input", default="data/raw_data.csv",
                        help="Caminho do CSV de entrada (default: data/raw_data.csv)")
    parser.add_argument("--reports-dir", default="reports",
                        help="Diretório de relatórios (default: reports)")
    parser.add_argument("--log-file", default="logs/pipeline.log",
                        help="Arquivo de log (default: logs/pipeline.log)")
    return parser.parse_args()


def main():
    args = parse_args()
    logger = setup_logger(args.log_file)

    logger.info("Inicio do pipeline")
    logger.info(f"Input: {args.input}")
    logger.info(f"Reports: {args.reports_dir}")
    logger.info(f"Log file: {args.log_file}")

    try:
        rows = read_csv(args.input)  # se falhar aqui, é erro operacional
        logger.info(f"Registros lidos: {len(rows)}")

        valid_rows, errors = validate_rows(rows)

        invalid_count = len(set(e.row_index for e in errors))
        logger.info(f"Validos: {len(valid_rows)}")
        logger.info(f"Invalidos: {invalid_count}")

        # Relatórios: se falhar, também é erro operacional (IO)
        valid_csv_path = f"{args.reports_dir}/valid_rows.csv"
        errors_json_path = f"{args.reports_dir}/errors.json"

        save_valid_rows_csv(valid_rows, valid_csv_path)
        save_errors_json(errors, errors_json_path)

        logger.info("Relatorios gerados com sucesso")
        logger.info(f"- {valid_csv_path}")
        logger.info(f"- {errors_json_path}")

        # Erros de validação são "tratáveis": WARNING
        for e in errors[:20]:
            logger.warning(f"Linha {e.row_index} | {e.field}: {e.message} (valor: {e.raw_value})")

        if errors:
            logger.info("Execucao concluida com avisos (dados invalidos detectados).")
        else:
            logger.info("Execucao concluida sem avisos.")

    except FileNotFoundError as e:
        logger.error(f"Falha operacional: arquivo nao encontrado. {e}")
    except ValueError as e:
        # CSV vazio/sem header etc.
        logger.error(f"Falha operacional: entrada invalida para processamento. {e}")
    except Exception as e:
        # Inesperado: bug, ambiente quebrado, etc.
        logger.critical("Falha critica inesperada no pipeline.", exc_info=True)


if __name__ == "__main__":
    main()

# Por que fiz assim e o que buscamos:

# main só orquestra: regra de ouro. Ele coordena, não faz trabalho pesado, o que deixa o código mais limpo e fácil de manter. Cada função tem uma responsabilidade clara.

# logger.info/warning/exception: níveis diferentes para separar “normal”, “problema tratável” e “erro sério”, o que é crucial pra análise de logs depois. Você pode filtrar por nível e entender rapidamente o que aconteceu.

# logger.exception: registra stack trace — isso é o que salva sua pele quando algo quebra, porque você tem o contexto completo do erro, não só a mensagem.

# limite de 20 erros exibidos: em produção você não despeja 10 mil linhas no console, isso é inútil. Mostrar um sample dos erros mais comuns já dá uma boa ideia do que está acontecendo, sem virar um caos.

# Isso nos ensina “produção de verdade”: previsível, rastreável e auditável, com logs claros e relatórios estruturados. O código é organizado para ser fácil de entender, manter e escalar, o que é essencial em pipelines de dados reais.