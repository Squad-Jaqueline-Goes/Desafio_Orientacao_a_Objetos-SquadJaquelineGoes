from classes.item_biblioteca import ItemBiblioteca
class Exemplar(ItemBiblioteca):
    def __init__(self, id, titulo, estado, max_renovacoes):
        super().__init__(id, titulo)
        self.__estado = estado
        self.__max_renovacoes = max_renovacoes
        self.__emprestimo_atual = None

    """
    A classe Exemplar herda da classe abstrata ItemBiblioteca e adiciona
    atributos específicos como o estado do exemplar e o número máximo de renovações
    permitidas. Além disso, oferece métodos para obter informações sobre o exemplar,
    atualizar seu estado, e associá-lo a um livro específico.
    """
    def get_informacoes(self):
        return {
            "id": self._id,
            "titulo": self._titulo,
            "estado": self.__estado,
            "max_renovacoes": self.__max_renovacoes,
            "livro": self.livro.titulo if hasattr(self, 'livro') else "Não associado a um livro"
        }

    """
    Retorna um dicionário contendo as informações do exemplar.

    O dicionário inclui o ID, título, estado, número máximo de renovações e,
    se disponível, o título do livro associado.
    """

    def atualizar_estado(self, estado):
        if estado not in ["disponível", "emprestado", "reservado"]:
            raise ValueError("Estado inválido")
        self.__estado = estado
        self._disponivel = (estado == "disponível")

    """
    Atualiza o estado do exemplar.

    O estado pode ser "disponível", "emprestado", ou "reservado". Se o estado
    fornecido for inválido, uma exceção será levantada.
    """

    @property
    def max_renovacoes(self):
        return self.__max_renovacoes

    @max_renovacoes.setter
    def max_renovacoes(self, max_renovacoes):
        self.__max_renovacoes = max_renovacoes

    def associar_livro(self, livro):
        self.livro = livro

    @property
    def emprestimo_atual(self):
        return self.__emprestimo_atual
    
    @emprestimo_atual.setter
    def emprestimo_atual(self, emprestimo):
        self.__emprestimo_atual = emprestimo

    def __str__(self):
        return f"Exemplar ID: {self._id}, Estado: {self.__estado}, Max Renov: {self.__max_renovacoes}, Disponível: {self._disponivel}"
