class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome or nome == '':
            raise ValueError('O Autor deve possuir um Nome')
        if not isinstance(nome, str):
            raise ValueError('Nome deve ser uma string')
        self._nome = nome

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        if not nacionalidade or nacionalidade == '':
            raise ValueError('O Autor deve possuir uma Nacionalidade')
        if not isinstance(nacionalidade, str):
            raise ValueError('Nacionalidade deve ser uma string')
        self._nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome} ({self.nacionalidade})"
