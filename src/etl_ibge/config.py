"""Configurações do projeto ETL IBGE"""

# url da API
IBGE_API_BASE = 'https://servicodados.ibge.gov.br/api/v1'

# Endpoints disponiveis
ENDPOINTS = {
    "estados": "/localidades/estados",
    "municipios": "/localidades/municipios",
    "regioes": "/localidades/regioes",
    "paises": "/localidades/paises",
    "pesquisa_urbana": "/pesquisas/Urbana",
    "indicadores": "/indicadores",
}

# Configurações de arquivo
OUTPUT_DIR = "data"
