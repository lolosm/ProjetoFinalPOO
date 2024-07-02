import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

class APINoticias:
    URL_API = "https://newsapi.org/v2/everything"

    @staticmethod
    def obter_noticias(palavra_chave):
        parametros = {
            "q": palavra_chave,
            "apiKey": API_KEY,
            "language": "pt"
        }
        resposta = requests.get(APINoticias.URL_API, params=parametros)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            raise Exception("Erro ao buscar notícias")
