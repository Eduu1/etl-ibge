import requests
import pandas as pd
from pathlib import Path
from etl_ibge.config import IBGE_API_BASE, ENDPOINTS, OUTPUT_DIR


def buscar_dados_ibge(endpoints: str) -> list:
    """
    Busca dados da API do IBGE

    Args:
        endpoints: Nome do endpoint (estados, municipios, regioes, paises)

    Returns:
        Lista de dicionarios com os dados

    """
    if endpoints not in ENDPOINTS:
        raise ValueError(
            f"Endpoint {endpoints} não existe. Use: {list(ENDPOINTS.keys())}")

    url = f"{IBGE_API_BASE}{ENDPOINTS[endpoints]}"
    print(f"Buscando dados de {endpoints}...")
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def salvar_csv(dados: list, endpoint: str):
    """
    Salvar os dados em arquivo CSV

    Args:
        dados: Lista de dicionarios com os dados
        endpoint: Nome do endpoint (para nome do arquivo)
    """
    Path(OUTPUT_DIR).mkdir(exist_ok=True)

    df = pd.DataFrame(dados)
    filename = f"{OUTPUT_DIR}/{endpoint}.csv"
    df.to_csv(filename, index=False, encoding='utf-8')

    print(f"Dados salvos em: {filename}")
    print(f"Total de registros: {len(dados)}")


def executar_etl(endpoints: str = "estados"):
    """
    Executa o pipeline ETL completo

    Args:
        endpoint: Qual endpoint da API buscar
    """
    try:
        # Extrair
        dados = buscar_dados_ibge(endpoints)

        # Transformar (Adicionar aqui)
        print(f"Dados extraidos: {len(dados)} registros")

        # Carregar
        salvar_csv(dados, endpoints)
        print("ETL executado com sucesso!")

    except Exception as e:
        print(f"Erro no ETL: {e}")


if __name__ == "__main__":
    executar_etl("paises")
