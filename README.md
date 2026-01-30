# data-validator-logger-for-ml-pipelines-python
Validação de dados e registros de log para ML.

A ideia principal é registrar logs, erros de validação de dados (propositalmente) e solucionar csv vazios ou inválidos.

Com dados em csv inválidos, pode se criar um reflexo de não confiança em inputs, mesmo parecendo legítimos. Modelos de IA quebram nestes pontos, assim podemos validar antes do erro ocorrer.

Com uso de validator e incluindo dados quebrados em csv, podemos verificar os erros apresentados na impressão para solucionar, mostrando onde estão, quais foram e porquê ocorreram.
