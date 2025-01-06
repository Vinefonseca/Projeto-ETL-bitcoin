import requests

def extract_dados_bitcoin():

    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados

def transform_dados_bitcoin(dados):

    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"] 
    moeda = dados["data"]["currency"]

    dados_transformados = {
        "valor" : valor,
        "criptomoeda" : criptomoeda,
        "moeda" : moeda
    }

    return dados_transformados

if __name__ == "_main_":
    # Extração dos Dados 
    dados_json = extract_dados_bitcoin()
    dados_tratados = transform_dados_bitcoin(dados_json)
    print(dados_tratados)