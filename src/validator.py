from dataclasses import dataclass
from typing import Any

REQUIRED_FIELDS = ["id", "idade", "renda", "email"]

@dataclass
class ValidationError:
    row_index: int
    field: str
    message: str
    raw_value: Any

def _to_int(value: Any) -> int:
    return int(str(value).strip())

def _to_float(value: Any) -> float:
    return float(str(value).strip().replace(",", "."))

def validate_rows(rows: list[dict]) -> tuple[list[dict], list[ValidationError]]:
    valid_rows: list[dict] = []
    errors: list[ValidationError] = []

    for i, row in enumerate(rows, start=1):
        row_has_error = False

        # 1) Campos obrigatórios
        for field in REQUIRED_FIELDS:
            if field not in row:
                errors.append(ValidationError(i, field, "campo ausente no CSV", None))
                row_has_error = True
            elif str(row[field]).strip() == "":
                errors.append(ValidationError(i, field, "valor vazio", row[field]))
                row_has_error = True

        if row_has_error:
            continue  # aqui faz sentido parar: faltou requisito básico

        # 2) Conversões + regras (agora SEM continue)
        try:
            rid = _to_int(row["id"])
            if rid <= 0:
                errors.append(ValidationError(i, "id", "deve ser > 0", row["id"]))
                row_has_error = True
        except (ValueError, TypeError):
            errors.append(ValidationError(i, "id", "não é inteiro válido", row["id"]))
            row_has_error = True

        try:
            idade = _to_int(row["idade"])
            if not (0 <= idade <= 120):
                errors.append(ValidationError(i, "idade", "fora do intervalo 0–120", row["idade"]))
                row_has_error = True
        except (ValueError, TypeError):
            errors.append(ValidationError(i, "idade", "não é inteiro válido", row["idade"]))
            row_has_error = True

        try:
            renda = _to_float(row["renda"])
            if renda < 0:
                errors.append(ValidationError(i, "renda", "não pode ser negativa", row["renda"]))
                row_has_error = True
        except (ValueError, TypeError):
            errors.append(ValidationError(i, "renda", "não é número válido", row["renda"]))
            row_has_error = True

        email = str(row["email"]).strip()
        if " " in email or "@" not in email or email.startswith("@") or email.endswith("@"):
            errors.append(ValidationError(i, "email", "email inválido (checagem simples)", row["email"]))
            row_has_error = True

        # 3) Só adiciona se passou em tudo
        if not row_has_error:
            valid_rows.append({
                "id": rid,
                "idade": idade,
                "renda": renda,
                "email": email
            })

    return valid_rows, errors
