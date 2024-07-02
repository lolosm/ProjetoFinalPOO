from gerenciador_de_dados import GerenciadorDeDadosJSON


class GerenciadorDeNoticias(GerenciadorDeDadosJSON):
    ARQUIVO_NOTICIAS = "noticias.json"

    @staticmethod
    def salvar_noticias(noticias):
        GerenciadorDeNoticias.salvar_dados(GerenciadorDeNoticias.ARQUIVO_NOTICIAS, noticias)

    @staticmethod
    def carregar_noticias():
        return GerenciadorDeNoticias.carregar_dados(GerenciadorDeNoticias.ARQUIVO_NOTICIAS)
