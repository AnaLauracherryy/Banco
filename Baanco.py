import sqlite3
import hashlib

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        try:
            c = self.conexao.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios(
                idusuario INTEGER PRIMARY KEY,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT,
                senha TEXT)""")
            self.conexao.commit()
            c.close()
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")

    def inserir_usuario(self, nome, telefone, email, usuario, senha):
        try:
            c = self.conexao.cursor()
            # Hash da senha
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            c.execute("INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
                      (nome, telefone, email, usuario, senha_hash))
            self.conexao.commit()
            c.close()
        except sqlite3.Error as e:
            print(f"Erro ao inserir o usuário: {e}")

    def fechar_conexao(self):
        self.conexao.close()

# Exemplo de uso
banco = Banco()
banco.inserir_usuario("Analaura", "123456789", "analaura@example.com", "analaura", "minhasenha")
banco.fechar_conexao()