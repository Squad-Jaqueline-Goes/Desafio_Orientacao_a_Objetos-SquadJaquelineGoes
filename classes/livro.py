from classes.autor import Autor  
from classes.exemplar import Exemplar  

class Livro:
    def __init__(self, titulo, editora, generos, autores, exemplares=None, num_maximo_renovacoes=None): # Cada livro tem um título, editora, uma lista de gêneros aos quais pertence e uma lista de exemplares disponíveis.
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares = exemplares
        self.autores = autores # Cada livro pode ter um ou mais autores.
        self.num_maximo_renovacoes = num_maximo_renovacoes # Alguns livros podem ter um número máximo de renovações permitidas.

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def editora(self):
        return self._editora

    @property
    def generos(self):
        return self._generos

    @property
    def autores(self):
        return self.__autores

    @property
    def exemplares(self):
        return self.__exemplares

    @property
    def num_maximo_renovacoes(self):
        return self.__num_maximo_renovacoes

    @titulo.setter
    def titulo(self, titulo):
        if not titulo or titulo == '':
            raise ValueError('O Livro deve possuir um Título')
        if not isinstance(titulo, str):
            raise ValueError('Título deve ser uma string')
        self._titulo = titulo

    @editora.setter
    def editora(self, editora):
        if not editora:
            raise ValueError('O Livro deve possuir uma Editora')
        if not isinstance(editora, str):
            raise ValueError('Editora deve ser uma string')
        self._editora = editora

    @generos.setter
    def generos(self, generos):
        if not generos or generos == [] or generos == '':
            raise ValueError('O Livro deve possuir pelo menos um Gênero')
        if isinstance(generos, str): # Se for uma string, transforma em lista
            generos = [generos]
        if not isinstance(generos, list): 
            raise ValueError('Gêneros deve ser uma lista')
        for genero in generos: 
            if not isinstance(genero, str):
                raise ValueError('Gênero deve ser uma string')
        self._generos = generos

    @exemplares.setter
    def exemplares(self, exemplares):
        if not exemplares or exemplares == '': # Se não tiver exemplares, cria uma lista vazia
            exemplares = []
        if not isinstance(exemplares, list): 
            raise ValueError('Exemplares deve ser uma lista')
        for exemplar in exemplares: 
            if not isinstance(exemplar, Exemplar):
                raise ValueError('Exemplar é do tipo incorreto')
        self.__exemplares = exemplares

    @num_maximo_renovacoes.setter
    def num_maximo_renovacoes(self, num_maximo_renovacoes):
        if num_maximo_renovacoes and num_maximo_renovacoes < 0: # Se tiver um número máximo de renovações, não pode ser negativo 
            raise ValueError('Número máximo de renovações não pode ser negativo')
        if num_maximo_renovacoes and not isinstance(num_maximo_renovacoes, int): 
            raise ValueError('Número máximo de renovações deve ser um inteiro')
        self.__num_maximo_renovacoes = num_maximo_renovacoes

    @autores.setter
    def autores(self, autores):
        if not autores or autores == [] or autores == '': 
            raise ValueError('O Livro deve possuir pelo menos um Autor')
        if isinstance(autores, Autor): # Se for um autor, transforma em lista
            autores = [autores]
        for autor in autores:
            if not isinstance(autor, Autor):
                raise ValueError('Autor é do tipo incorreto')
        self.__autores = autores

    def adicionar_exemplar(self, exemplar):
        if exemplar in self.__exemplares: # Verifica se o exemplar já está na lista
            raise ValueError('O exemplar já está na lista de exemplares.')
        self.__exemplares.append(exemplar) # Adiciona o exemplar a lista
    
    def remover_exemplar(self, exemplar):
        """Remove um exemplar da lista de exemplares."""
        if exemplar not in self.__exemplares:
            raise ValueError('O exemplar especificado não está na lista de exemplares.')
        self.__exemplares.remove(exemplar)

    # IMPLEMENTAR: método para verificar se um livro está disponível

    def verificar_disponibilidade(self):
        # Retorna True se houver pelo menos um exemplar disponível, False caso contrário
        return any(exemplar.get_informacoes()['estado'] == "disponível" for exemplar in self.exemplares)

    def __str__(self):
        autores_str = ""
        for autor in self.autores:
            autores_str += str(autor) + ", "
        autores_str = autores_str[:-2]  # Remove a última vírgula e espaço

        generos_str = ""
        for genero in self.generos:
            generos_str += genero + ", "
        generos_str = generos_str[:-2]  # Remove a última vírgula e espaço

        exemplares_count = len(self.exemplares) if self.exemplares else 0
        max_renovacoes = self.num_maximo_renovacoes if self.num_maximo_renovacoes is not None else 'Sem limite'

        return (f"Título: {self.titulo}, \n"
                f"Editora: {self.editora}, \n"
                f"Gêneros: {generos_str}, \n"
                f"Autores: {autores_str}, \n"
                f"Exemplares: {exemplares_count}, \n"
                f"Número Máximo de Renovações: {max_renovacoes}")
