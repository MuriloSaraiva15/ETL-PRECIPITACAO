🌧️ Projeto de Análise de Precipitação (2025)

Este projeto realiza uma análise exploratória de dados (EDA) de precipitação diária de uma cidade ao longo do ano de 2025, utilizando Python.

O foco está na limpeza de dados, agregação, insights estatísticos e visualização, gerando tanto resumos numéricos quanto gráficos de alta qualidade. O projeto foi desenvolvido para fins de aprendizado, apresentação de portfólio e reprodutibilidade, seguindo uma separação clara entre os scripts de processamento de dados e de visualização.
📂 Estrutura do Projeto
Plaintext

    ├── dados-precipitacao.csv        # Dataset bruto de precipitação
    ├── dados.py                      # Carregamento, limpeza e análise central
    ├── grafico_chuva_diaria.py       # Visualização da série temporal diária
    ├── grafico_chuva_mensal.py       # Gráfico de chuva acumulada mensal
    ├── grafico_chuva_estacacoes.py   # Gráficos de distribuição sazonal
    ├── graficos/                     # Gráficos gerados (criados automaticamente)
    └── README.md

📊 Conjunto de Dados (Dataset)

    Fonte: Medições de uma estação meteorológica

    Período: Janeiro–Dezembro de 2025

    Granularidade: Precipitação diária (mm)

Colunas principais utilizadas:

    Data → Data da medição

    Valor → Quantidade de chuva em milímetros (mm)

    Colunas de metadados irrelevantes são removidas durante o pré-processamento.

⚙️ Processamento de Dados (dados.py)

O módulo dados.py é responsável por:

    Carregar o arquivo CSV.

    Limpar e formatar os dados.

    Converter tipos de dados (datas e valores numéricos).

    Remover colunas não utilizadas.

    Realizar análise descritiva, incluindo:

        Precipitação total anual.

        Média diária de chuva.

        Precipitação apenas em dias chuvosos.

        Contagem de dias com e sem chuva.

        Agregação semanal, mensal e sazonal.

        Top 10 dias mais chuvosos e menos chuvosos.

O módulo também expõe uma função reutilizável:
Python

def carregar_dados():
    ...

Essa função é utilizada por todos os scripts de visualização para garantir a consistência dos dados.
📈 Visualizações

Todos os gráficos são salvos automaticamente no diretório graficos/.
1️⃣ Chuva Diária – Série Temporal

Arquivo: grafico_chuva_diaria.py

    Gráfico de linha da precipitação diária.

    Destaque para os dias com chuva.

    Inclui: Média diária geral e média considerando apenas dias chuvosos.

    Marcadores mensais no eixo X.

    📌 Saída: precipitacao_diaria.png

2️⃣ Acumulado Mensal de Chuva

Arquivo: grafico_chuva_mensal.py

    Gráfico de barras mostrando o total de chuva por mês.

    Exibe os totais mensais e a linha de média mensal geral como referência.

    Nomes dos meses formatados em português.

    📌 Saída: media_mensal.png

3️⃣ Distribuição Sazonal (Estações)

Arquivo: grafico_chuva_estacacoes.py

    Dois gráficos de pizza: Precipitação total por estação e média diária por estação.

    Estações consideradas: Verão, Outono, Inverno e Primavera.

    📌 Saída: pizza_estacoes.png

🧰 Tecnologias Utilizadas

    Python 3

    pandas – manipulação de dados

    matplotlib – plotagem de gráficos

    seaborn – visualizações estatísticas

    calendar / locale – formatação de nomes de meses

▶️ Como Executar

    Instale as dependências:
    Bash

    pip install pandas matplotlib seaborn

    Execute a análise e as visualizações:
    Bash

    python grafico_chuva_diaria.py
    python grafico_chuva_mensal.py
    python grafico_chuva_estacacoes.py

Todos os gráficos serão salvos automaticamente.
🎯 Objetivos do Projeto

    Praticar conceitos de ETL com dados reais de séries temporais.

    Aplicar técnicas de agregação e amostragem (resampling) de dados.

    Produzir visualizações claras e prontas para apresentações.

    Construir um projeto de análise de dados sólido para portfólio.

📌 Notas: O projeto separa intencionalmente a lógica de análise da lógica de visualização, tornando os scripts modulares e reutilizáveis. Ideal para portfólios de Analista de Dados Júnior ou Engenharia de Dados.
