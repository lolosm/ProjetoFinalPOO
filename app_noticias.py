import tkinter as tk
from tkinter import messagebox
import webbrowser
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
        self.root.geometry("830x600")
        self.root.configure(background='#f0f0f0')

        titulo = tk.Label(self.root, text="App de Notícias", font=('Helvetica', 24, 'bold'), background='#f0f0f0', fg='#333333')
        titulo.pack(pady=20)

        frame_entradas = tk.Frame(self.root, background='#f0f0f0')
        frame_entradas.pack(pady=10)

        tk.Label(frame_entradas, text="Palavra-chave:", background='#f0f0f0', font=('Helvetica', 14)).grid(row=0, column=0, padx=10, pady=5)
        self.campo_palavra_chave = tk.Entry(frame_entradas, font=('Helvetica', 14), width=30)
        self.campo_palavra_chave.grid(row=0, column=1, padx=10, pady=5)

        botao_buscar = tk.Button(self.root, text="Buscar Notícias", command=self.buscar_e_exibir_noticias, bg='#00008B', fg='white', font=('Helvetica', 12), width=20)
        botao_buscar.pack(pady=10)

        self.frame_canvas = tk.Frame(self.root, background='#f0f0f0')
        self.frame_canvas.pack(pady=10, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_canvas, background='#f0f0f0', bd=0, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_noticias = tk.Frame(self.canvas, background='#f0f0f0')
        self.canvas.create_window((0, 0), window=self.frame_noticias, anchor="nw")

        self.frame_noticias.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

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
            for widget in self.frame_noticias.winfo_children():
                widget.destroy()

            for noticia in noticias:
                titulo = noticia["title"]
                descricao = noticia["description"]
                url = noticia["url"]

                noticia_frame = tk.Frame(self.frame_noticias, background='#ffffff', bd=1, relief=tk.SOLID)
                noticia_frame.pack(pady=10, padx=10, fill=tk.X, expand=True)

                label_titulo = tk.Label(noticia_frame, text=titulo, font=('Helvetica', 16, 'bold'), background='#ffffff', wraplength=750, justify=tk.LEFT, fg='#333333')
                label_titulo.pack(anchor='w', padx=10, pady=5)

                label_descricao = tk.Label(noticia_frame, text=descricao, font=('Helvetica', 14), background='#ffffff', wraplength=750, justify=tk.LEFT, fg='#666666')
                label_descricao.pack(anchor='w', padx=10, pady=5)

                botao_link = tk.Button(noticia_frame, text="Leia mais", command=lambda url=url: webbrowser.open(url), bg='#4169E1', fg='white', font=('Helvetica', 12), width=15)
                botao_link.pack(anchor='e', padx=10, pady=5)

            self.on_frame_configure(None)
            GerenciadorDeNoticias.salvar_noticias(noticias)
        else:
            messagebox.showinfo("Informação", "Nenhuma notícia encontrada.")
