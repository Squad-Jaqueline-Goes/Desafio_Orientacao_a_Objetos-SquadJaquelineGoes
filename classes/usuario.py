from classes.pessoa import Pessoa
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)

    def exibir_dados(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}"

    def __str__(self):
        return self.exibir_dados()
