# Data Validator & Logger for ML Pipelines (Python)

- Contexto

Este projeto foi desenvolvido com o objetivo de simular um pipeline inicial de preparação de dados para Machine Learning, com foco em validação, tratamento de erros, logging estruturado e previsibilidade de execução.

Em ambientes reais, dados são recebidos de múltiplas fontes (APIs, planilhas, bancos de dados, uploads externos). Se esses dados estiverem malformados, incompletos ou inconsistentes, o modelo de Machine Learning pode aprender padrões incorretos, gerar decisões imprecisas ou até introduzir vulnerabilidades no sistema.

Este projeto parte do seguinte problema:

> “Se os dados de entrada estiverem quebrados ou inconsistentes, o modelo aprende errado — e isso pode se tornar uma falha sistêmica.”

---

- Objetivo

Construir um sistema em Python capaz de:

- Ler arquivos CSV
- Validar estrutura e conteúdo dos dados
- Detectar inconsistências propositalmente inseridas
- Registrar logs detalhados de execução
- Gerar relatórios de dados válidos e inválidos

O foco principal é garantir que a entrada de dados seja confiável antes de alimentar qualquer modelo de IA.

---

- Conceitos Aplicados

Este projeto trabalha conceitos fundamentais de engenharia de dados e segurança:

- Validação de input (input validation)
- Separação entre erros estruturais e erros de conteúdo
- Tratamento de exceções controlado
- Logging com rastreabilidade
- Geração de relatórios auditáveis
- Testes automatizados com `unittest`

A validação é feita em duas camadas:

1. **Estrutural**: campos obrigatórios ausentes ou vazios.
2. **Conteúdo**: tipos inválidos, valores fora de intervalo, e-mails malformados etc.

Essa abordagem simula práticas utilizadas em pipelines reais e prepara o terreno para aplicações em AI Security.

---

- Estrutura do Projeto
data-validator/
│
├── data/
│ └── raw_data.csv
│
├── logs/
│ └── pipeline.log
│
├── reports/
│ ├── valid_rows.csv
│ └── errors.json
│
├── src/
│ ├── reader.py
│ ├── validator.py
│ ├── logger.py
│ ├── report.py
│ └── main.py
│
├── tests/
│ └── test_validator.py
│
└── README.md

⚙️ Como Executar

- Executar o pipeline:

```bash
python src/main.py
Isso irá:

Ler o arquivo CSV

Validar os dados

Gerar logs em logs/pipeline.log

Gerar relatórios em reports/

- Executar os testes automatizados:
python -m unittest discover -s tests
- Saídas Geradas
valid_rows.csv → registros considerados válidos
errors.json → lista detalhada de erros encontrados
pipeline.log → histórico estruturado da execução

- Conexão com Segurança e AI Security
Este projeto reforça um princípio fundamental:

Não confiar em inputs externos, mesmo que pareçam legítimos.

Modelos de IA são sensíveis à qualidade dos dados. Dados inconsistentes podem gerar:

vieses

decisões incorretas

comportamento imprevisível

superfícies de ataque indiretas

A validação prévia reduz esses riscos e aumenta a robustez do sistema.

- Próximos Passos
Possíveis evoluções do projeto:

Integração com um modelo simples de Machine Learning

Validação configurável via JSON

Implementação de CLI com argumentos

Validação avançada de e-mails (regex)

Integração com biblioteca de tipagem como Pydantic

Simulação de dataset adversarial

- Propósito Acadêmico
Este projeto faz parte de uma jornada prática de aprendizado em:

Engenharia de Software

Estruturação de pipelines de dados

Fundamentos de segurança aplicada a IA

O objetivo não é apenas validar dados, mas desenvolver pensamento crítico sobre confiabilidade, rastreabilidade e previsibilidade de sistemas.