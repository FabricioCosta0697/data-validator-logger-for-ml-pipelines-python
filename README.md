# data-validator-logger-for-ml-pipelines-python
Ideia central do projeto: construir um sistema em Python que prepara dados para Machine Learning, com foco em:
validação;
tratamento de erro;
logs;
previsibilidade.

O problema a ser resolvido: 
“Recebo dados de várias fontes para treinar um modelo.
Se esses dados estiverem quebrados, enviesados ou malformados, o modelo aprende errado — e isso vira vulnerabilidade.”  

Registrar logs, erros de validação de dados (propositalmente) e solucionar arquivos csv (Comma-Separated Values, ou Valores Separados por Vírgula) vazios ou inválidos.

Com dados em csv inválidos, pode se criar um reflexo de não confiança em inputs, mesmo parecendo legítimos. Modelos de IA quebram nestes pontos, assim podemos validar antes do erro ocorrer.

Com uso de validator e incluindo dados quebrados em csv, podemos verificar os erros apresentados na impressão para solucionar, mostrando onde estão, quais foram e porquê ocorreram.
