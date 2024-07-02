import json
import os


class GerenciadorDeDadosJSON:
    @staticmethod
    def salvar_dados(nome_arquivo, dados):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    @staticmethod
    def carregar_dados(nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as arquivo:
                return json.load(arquivo)
        return []
