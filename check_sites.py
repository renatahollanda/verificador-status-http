import requests
import os
from time import sleep
from datetime import datetime


def verificar_status_site(arquivo_entrada, arquivo_saida):
    """
    Verifica o status HTTP de uma lista de sites e salva os resultados.

    Args:
        arquivo_entrada (str): Caminho do arquivo com lista de sites.
        arquivo_saida (str): Caminho do arquivo para salvar o resultado.
    """

    # Verificar/Cria arquivo de saída
    if not os.path.exists(arquivo_saida):
        with open(arquivo_saida, 'w') as fout:
            fout.write("URL;STATUS_CODE;TIMESTAMP\n")

    # Lê os sites linha a linha do arquivo .txt
    try:
        with open(arquivo_entrada, 'r') as fin:
            sites = [linha.strip() for linha in fin if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return

    # Analisa cada URL
    resultados = {}
    for site in sites:
        # Adiciona http:// se não houver protocolo especificado
        if not site.startswith(("http://", "https://")):
            site = f"http://{site}"

        try:
            resposta = requests.get(site, timeout=10)
            status = resposta.status_code
            sleep(0.5)
        except requests.exceptions.RequestException as erro:
            status = f'Erro: {str(erro)}'

        resultados[site] = status
        print(f"[{site}] -> {status}")

    # Salva os resultados
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        with open(arquivo_saida, 'a') as fout:
            for site, status in resultados.items():
                fout.write(f'{site};{status};{timestamp}\n')
        print(f"\nResultados salvos em: {arquivo_saida}")
    except IOError as erro:
        print(f"Erro aos salvar resultados: {str(erro)}")


if __name__ == "__main__":
    ARQUIVO_ENTRADA = "sites.txt"
    ARQUIVO_SAIDA = "sites_status.csv"

    print("\nVERIFICADOR DE STATUS DE SITES")
    print(f"Lendo sites de: {ARQUIVO_ENTRADA}")
    print(f"Salvando resultados em: {ARQUIVO_SAIDA}\n")

    verificar_status_site(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)
