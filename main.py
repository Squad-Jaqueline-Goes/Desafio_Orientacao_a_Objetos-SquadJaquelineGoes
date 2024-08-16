from classes.pessoa import Pessoa
from classes.usuario import Usuario
from classes.autor import Autor  
from classes.livro import Livro
from classes.exemplar import Exemplar 
from classes.emprestimo import Emprestimo
from datetime import datetime

try:
    # autor
    autor1 = Autor('Fulano', 'Brasileiro') 
    autor2 = Autor('Ciclano', 'Brasileiro')
    print('\n--- CRIANDO AUTOR ----')
    print(autor1)
    print(autor2)

    # livro
    print('\n--- CRIANDO LIVRO ----')
    autores = [autor1, autor2]
    livro = Livro('Python para iniciantes', 'Editora A', 'Tecnologia', autores) 
    print(livro)

    # usuário
    print('\n--- CRIANDO USUARIO ----')
    usuario = Usuario('Fulano', '123456789', 'Brasileiro') 
    print(usuario)

    # exemplar
    print('\n--- CRIANDO EXEMPLAR ----')
    exemplar1 = Exemplar("1", "Python para iniciantes", "disponível", 2)
    exemplar2 = Exemplar("2", "Python para iniciantes", "disponível", 2)
    print(exemplar1)
    print(exemplar2)

    # associar livro ao exemplar
    print('\n--- ASSOCIANDO LIVRO AO EXEMPLAR ----')
    livro.adicionar_exemplar(exemplar1)
    livro.adicionar_exemplar(exemplar2)
    print(livro)

    # empréstimo
    print('\n--- CRIANDO EMPRESTIMO ----')
    data_emprestimo = datetime.strptime('01/01/2021', '%d/%m/%Y').date()
    data_devolucao = datetime.strptime('01/02/2021', '%d/%m/%Y').date()
    emprestimo = Emprestimo(data_emprestimo, data_devolucao, usuario, exemplar1, False)


   
except Exception as e:
    print(e)