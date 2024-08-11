from classes.usuario import Usuario
from classes.exemplar import Exemplar


class Emprestimo:
    def __init__(self, data_emprestimo, data_devolucao, usuario, exemplar):
        if not isinstance(usuario):
            raise ValueError("usuario deve ser uma instância da classe Usuario")
        if not isinstance(exemplar):
            raise ValueError("exemplar deve ser uma instância da classe Exemplar")

        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__usuario = usuario
        self.__exemplar = exemplar


    """
    A classe Emprestimo gerencia as informações relacionadas ao empréstimo, como as
    datas de empréstimo e devolução, o usuário que realizou o empréstimo, e o exemplar
    que foi emprestado. Também fornece métodos para registrar o empréstimo e a devolução
    de exemplares.
    """
    @property
    def data_emprestimo(self):
        return self.__data_emprestimo

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    @property
    def usuario(self):
        return self.__usuario

    @property
    def exemplar(self):
        return self.__exemplar


    """
    Registra o empréstimo do exemplar, alterando seu estado para "emprestado".
    Se o exemplar estiver disponível, o método altera seu estado para "emprestado"
    e retorna True. Caso contrário, lança uma exceção.
    """

    def registrar_emprestimo(self):
        if self.__exemplar.get_informacoes()['estado'] == "disponível":
            self.__exemplar.atualizar_estado("emprestado")
            return True
        raise Exception("O exemplar não está disponível para empréstimo")


    """
    Registra a devolução do exemplar, alterando seu estado para "disponível".
    Se o exemplar estiver emprestado, o método altera seu estado para "disponível"
    e retorna True. Caso contrário, lança uma exceção.
    """

    def registrar_devolucao(self):
        if self.__exemplar.get_informacoes()['estado'] == "emprestado":
            self.__exemplar.atualizar_estado("disponível")
            return True
        raise Exception("O exemplar já foi devolvido ou não foi emprestado")
