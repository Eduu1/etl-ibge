# ETL IBGE – Ingestão de Dados Públicos

Pipeline ETL em Python para **extração de dados públicos da API do IBGE**, transformação básica e persistência em arquivos CSV, seguindo boas práticas de estruturação de projetos e gerenciamento de dependências com **Poetry**.

---

## Objetivo do Projeto

Este projeto tem como objetivo demonstrar:
- Consumo de **API pública oficial (IBGE)**
- Estruturação de um **pipeline ETL simples**
- Organização de projeto Python
- Uso de **Poetry** para gerenciamento de dependências
- Geração de dados prontos para análise (CSV)

---


## Fonte dos Dados

Os dados são obtidos diretamente da **API pública do IBGE**:

- Estados
- Municípios
- Países
- Regiões

### Documentação oficial:  
https://servicodados.ibge.gov.br/api/docs/localidades

---

## Tecnologias Utilizadas

- Python 3.13+
- Poetry
- Requests
- Pandas
- API IBGE

---

## Como Executar o Projeto

### Clonar o repositório
```bash
git clone https://github.com/Eduu1/etl-ibge.git
cd etl-ibge

```

### Instalar dependências
```
poetry install

```

### Executar o ETL
```
poetry run python -m etl_ibge.etl

```
### Saída dos Dados

Os dados extraídos são salvos na pasta:
```
data/

```
