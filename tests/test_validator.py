import unittest
from src.validator import validate_rows

class TestValidator(unittest.TestCase):

    def test_valid_row(self):
        rows = [
            {"id": "1", "idade": "25", "renda": "3500.50", "email": "teste@email.com"}
        ]

        valid_rows, errors = validate_rows(rows)

        self.assertEqual(len(valid_rows), 1)
        self.assertEqual(len(errors), 0)

    def test_invalid_id(self):
        rows = [
            {"id": "abc", "idade": "25", "renda": "3500.50", "email": "teste@email.com"}
        ]

        valid_rows, errors = validate_rows(rows)

        self.assertEqual(len(valid_rows), 0)
        self.assertGreater(len(errors), 0)

    def test_multiple_errors_same_row(self):
        rows = [
            {"id": "abc", "idade": "", "renda": "-10", "email": "invalido"}
        ]

        valid_rows, errors = validate_rows(rows)

        self.assertEqual(len(valid_rows), 0)
        self.assertGreaterEqual(len(errors), 3)

if __name__ == "__main__":
    unittest.main()


# Por que fiz assim e o que estamos aprendendo:

# 1.Teste isolado
# Não estamos lendo CSV. Estamos testando somente o comportamento do validator.

# Isso treina:
# separação de responsabilidades;
# testes unitários reais.

# 2. Dois cenários básicos:

# Um caso válido
# Um caso inválido

# Segurança vive de cenários limítrofes (fronteiras de segurança).

# 3 Assert simples e direto

# Nada complexo, apenas validando:

# quantidade de válidos
# presença de erro

# Para rodar o teste utilizamos no terminal, na raiz do projeto:
# python -m unittest discover -s tests ou python -m unittest tests/test_validator.py