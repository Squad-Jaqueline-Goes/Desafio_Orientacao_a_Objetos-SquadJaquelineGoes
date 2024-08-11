from classes.pessoa import Pessoa
from classes.usuario import Usuario
from classes.autor import Autor  
from classes.livro import Livro
from classes.exemplar import Exemplar 
from classes.emprestimo import Emprestimo


try:
    # testes
    autor1 = Autor('Fulano', 'Brasileiro', '123456789') 
    autor2 = Autor('Ciclano', 'Brasileiro', '987654321')
    autores = [autor1, autor2]
    livro = Livro('Python para iniciantes', 'Editora A', 'Tecnologia', autores) # caso que funciona

    # testando algumas exceções
    livro = Livro('', 'Editora A', 'Tecnologia', autores, 2) # erro: O Livro deve possuir um Título
    livro = Livro('Python para Iniciantes', '', ['Tecnologia'], autores)  # Erro: O Livro deve possuir uma Editora
    livro = Livro('Python para Iniciantes', 'Editora A', [123], autores)  # Erro: Gênero deve ser uma string
    exemplares_invalidos = [1, 2, 3]
    livro = Livro('Python para Iniciantes', 'Editora A', ['Tecnologia'], autores, exemplares_invalidos)  # Erro: Exemplar é do tipo incorreto
    livro = Livro('Python para Iniciantes', 'Editora A', ['Tecnologia'], autores, num_maximo_renovacoes=-1)  # Erro: Número máximo de renovações não pode ser negativo
    livro = Livro('Python para Iniciantes', 'Editora A', ['Tecnologia'], autores, num_maximo_renovacoes='três')  # Erro: Número máximo de renovações deve ser um inteiro
    autores_invalidos = ['não é um Autor']
    livro = Livro('Python para Iniciantes', 'Editora A', ['Tecnologia'], autores_invalidos)  # Erro: Autor é do tipo incorreto

except Exception as e:
    print(e)