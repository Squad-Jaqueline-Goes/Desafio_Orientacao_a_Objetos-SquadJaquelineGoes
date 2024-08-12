from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, telefone, nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome or nome == '':
            raise ValueError('O Nome é obrigatório')
        if not isinstance(nome, str):
            raise ValueError('Nome deve ser uma string')
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        if not telefone or telefone == '':
            raise ValueError('O Telefone é obrigatório')
        if not isinstance(telefone, str):
            raise ValueError('Telefone deve ser uma string')
        self._telefone = telefone

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        if not nacionalidade or nacionalidade == '':
            raise ValueError('A Nacionalidade é obrigatória')
        if not isinstance(nacionalidade, str):
            raise ValueError('Nacionalidade deve ser uma string')
        self._nacionalidade = nacionalidade

    @abstractmethod
    def exibir_dados(self):
        pass  # Método abstrato que deve ser implementado nas subclasses
