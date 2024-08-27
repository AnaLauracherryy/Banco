import tkinter
from tkinter import *

class principal:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()
        self.titulo = Label(self.janela, text="pagina inicial")
        self.titulo["font"] = ("Arial", "29", "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.autenticar = Button(self.janela2)
        self.autenticar["text"] = "usuario"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()

        self.autenticar = Button(self.janela2)
        self.autenticar["text"] = "cidades"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()

        self.autenticar = Button(self.janela2)
        self.autenticar["text"] = "clientes"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()

        self.autenticar = Button(self.janela2)
        self.autenticar["text"] = "fechar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack(side=LEFT)

        self.mensagem = Label(self.janela4, text="", font=self.fontePadrao)
        self.mensagem.pack()
    def verificarSenha(self):
        usuario = self.nome.get()
        senha  = self.senha.get()
        if usuario == "usuarioSenai" and senha == "123456":
           self.mensagem["text"] = "autenticado"
        else:
           self.mensagem["text"] = "Erro na autenticacao"

root = Tk()
principal(root)
root.mainloop()