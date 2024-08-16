from classes.usuario import Usuario
from classes.exemplar import Exemplar


class Emprestimo:
    def __init__(self, data_emprestimo, data_devolucao, usuario, exemplar, renovar_emprestimo):
        if not isinstance(usuario, Usuario):
            raise ValueError("usuario deve ser uma instância da classe Usuario")
        if not isinstance(exemplar, Exemplar):
            raise ValueError("exemplar deve ser uma instância da classe Exemplar")

        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__usuario = usuario
        self.__exemplar = exemplar
        self.__renovar_empresatimo = renovar_emprestimo


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
    
    @property
    def renovar_emprestimo(self):
        return self.__renovar_empresatimo


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
    
    """
    Renova o empréstimo, estendendo a data de devolução.
    A renovação só é possível se o exemplar estiver atualmente emprestado.
    """

    def renovar_emprestimo(self, dias_adicionais):
        if self.__exemplar.get_informacoes()['estado'] == "emprestado":
            data_ordinal = self.__data_devolucao.toordinal()
            novo_data_ordinal = data_ordinal + dias_adicionais
            nova_data_devolucao = self.__data_devolucao.fromordinal(novo_data_ordinal)
            self.__data_devolucao = nova_data_devolucao
            return True
        raise Exception("Não é possível renovar o empréstimo porque o exemplar não está emprestado.")
