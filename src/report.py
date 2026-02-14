import csv
import json
import os
from dataclasses import asdict

def save_valid_rows_csv(valid_rows: list[dict], path: str = "reports/valid_rows.csv") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Mesmo sem dados, gerar arquivo com header ajuda no pipeline
    if not valid_rows:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("id,idade,renda,email\n")
        return

    fieldnames = list(valid_rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_rows)

def save_errors_json(errors: list, path: str = "reports/errors.json") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    payload = [asdict(e) if hasattr(e, "__dataclass_fields__") else e for e in errors]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

# Por que fiz assim e o que buscamos:

# CSV para válidos: fácil de abrir, usar em outros sistemas, alimentar ML depois, etc. CSV é o “idioma universal” dos dados tabulares.

# JSON para erros: estrutura rica, perfeita para auditoria, dashboards, debug e até automação de correção. Com JSON, você pode guardar detalhes como campo, mensagem, valor bruto, etc., sem se preocupar com formatação complicada.

# Criar pasta automaticamente: evita erro chato de “não existe diretório” e torna o processo mais fluido.

# Salvar header mesmo vazio: pipeline real odeia “arquivo faltando”; header fixo padroniza integração com próximos estágios, mesmo quando não tem dados válidos. Assim, o pipeline é mais robusto e previsível.

# asdict em dataclass: transforma seus ValidationError em JSON bonitinho sem gambiarra, mantendo o código limpo e fácil de manter.

# Isso treina mentalidade de “pipeline”: saída limpa para o próximo estágio, com formatos adequados para cada tipo de dado (CSV para tabular, JSON para estruturado).

# Beneficios do Pipeline de CI/CD (Continuous Integration/Continuous Deployment): 
# Automação: Reduz erros humanos ao eliminar tarefas manuais.
# Velocidade: Acelera a entrega de novas funcionalidades.
# Feedback Rápido: Identifica falhas e bugs imediatamente durante o processo de build.
# Consistência: Garante que o software seja compilado e testado da mesma forma sempre. 