from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):

    """
    A classe ItemBiblioteca fornece a estrutura básica para todos os itens
    da biblioteca, como livros e exemplares. Ela define atributos comuns,
    como ID, título, e disponibilidade, e exige que subclasses implementem
    métodos específicos para obter informações detalhadas e atualizar o estado
    do item.


    """

    def __init__(self, id, titulo):
        self._id = id
        self._titulo = titulo
        self._disponivel = True

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def disponivel(self):
        return self._disponivel

    @abstractmethod
    def get_informacoes(self):
        pass

    @abstractmethod
    def atualizar_estado(self, estado):
        pass

    def __str__(self):
        return f"Item Biblioteca(ID: {self._id}, Título: {self._titulo}, Disponível: {self._disponivel})"
