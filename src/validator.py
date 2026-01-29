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

    for i, row in enumerate(rows, start=1):  # start=1 pra bater com “linha humana”
        # 1) Campos obrigatórios
        for field in REQUIRED_FIELDS:
            if field not in row:
                errors.append(ValidationError(i, field, "campo ausente no CSV", None))
                continue
            if str(row[field]).strip() == "":
                errors.append(ValidationError(i, field, "valor vazio", row[field]))

        # Se já faltou campo, nem tenta converter (evita erro em cascata)
        if any(e.row_index == i and e.message in ("campo ausente no CSV", "valor vazio") for e in errors):
            continue

        # 2) Conversões + regras
        try:
            rid = _to_int(row["id"])
            if rid <= 0:
                errors.append(ValidationError(i, "id", "deve ser > 0", row["id"]))
        except Exception:
            errors.append(ValidationError(i, "id", "não é inteiro válido", row["id"]))
            continue

        try:
            idade = _to_int(row["idade"])
            if not (0 <= idade <= 120):
                errors.append(ValidationError(i, "idade", "fora do intervalo 0–120", row["idade"]))
        except Exception:
            errors.append(ValidationError(i, "idade", "não é inteiro válido", row["idade"]))

        try:
            renda = _to_float(row["renda"])
            if renda < 0:
                errors.append(ValidationError(i, "renda", "não pode ser negativa", row["renda"]))
        except Exception:
            errors.append(ValidationError(i, "renda", "não é número válido", row["renda"]))

        email = str(row["email"]).strip()
        if "@" not in email or email.startswith("@") or email.endswith("@"):
            errors.append(ValidationError(i, "email", "email inválido (checagem simples)", row["email"]))

        # 3) Se essa linha não gerou erro, normaliza e aceita
        if not any(e.row_index == i for e in errors):
            valid_rows.append({
                "id": rid,
                "idade": idade,
                "renda": renda,
                "email": email
            })

    return valid_rows, errors
