import tkinter as tk
from tkinter import messagebox
from api_noticias import APINoticias
from gerenciador_de_noticias import GerenciadorDeNoticias


class AppNoticias:
    def __init__(self, root):
        self.root = root
        self.init_tela_inicial()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def init_tela_inicial(self):
        self.limpar_tela()
        self.root.title("App de Notícias")
        self.root.geometry("700x600")
        self.root.configure(background='#B0E0E6')

        titulo = tk.Label(self.root, text="App de Notícias", font=('Arial', 20, 'bold'), background='#B0E0E6')
        titulo.pack(pady=20)

        frame_entradas = tk.Frame(self.root, background='#B0E0E6')
        frame_entradas.pack(pady=10)

        tk.Label(frame_entradas, text="Palavra-chave:", background='#B0E0E6', font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=5)
        self.campo_palavra_chave = tk.Entry(frame_entradas, font=('Arial', 14))
        self.campo_palavra_chave.grid(row=0, column=1, padx=10, pady=5)

        botao_buscar = tk.Button(self.root, text="Buscar Notícias", command=self.buscar_e_exibir_noticias, bg='#008CBA', fg='white', font=('Arial', 12))
        botao_buscar.pack(pady=10)

        frame_noticias = tk.Frame(self.root, background='#B0E0E6')
        frame_noticias.pack(pady=10)

        self.texto_resultado = tk.Text(frame_noticias, height=20, width=80, wrap=tk.WORD, background='#E0FFFF', font=('Arial', 14))
        self.texto_resultado.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

    def buscar_e_exibir_noticias(self):
        palavra_chave = self.campo_palavra_chave.get()

        if not palavra_chave:
            messagebox.showerror("Erro", "Por favor, insira uma palavra-chave.")
            return

        try:
            noticias = APINoticias.obter_noticias(palavra_chave)["articles"]
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar notícias: {str(e)}")
            return

        if noticias:
            self.texto_resultado.delete(1.0, tk.END)
            for noticia in noticias:
                titulo = noticia["title"]
                descricao = noticia["description"]
                url = noticia["url"]

                self.texto_resultado.insert(tk.END, f"Título: {titulo}\n")
                self.texto_resultado.insert(tk.END, f"Descrição: {descricao}\n")
                self.texto_resultado.insert(tk.END, f"Link: {url}\n\n")

            GerenciadorDeNoticias.salvar_noticias(noticias)
        else:
            messagebox.showinfo("Informação", "Nenhuma notícia encontrada.")
