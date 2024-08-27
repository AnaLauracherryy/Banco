from Banco import Banco
class Application:

    def __init__(self, idusuario = 0, nome = "", telefone = "",
        email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" +
            self.telefone + "', '" + self.email + "', '" +
            self.usuario + "', '" + self.senha + "' )")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_usuarios set nome = '" + self.nome + "',telefone = '" + self.telefone + "', email = '" + self.email +
            "', usuario = '" + self.usuario + "', senha = '" + self.senha +
            "' where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

