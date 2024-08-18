from classes.pessoa import Pessoa
from classes.usuario import Usuario
from classes.autor import Autor  
from classes.livro import Livro
from classes.exemplar import Exemplar 
from classes.emprestimo import Emprestimo
from datetime import datetime

#autor
def criar_autores():
    autor1 = Autor('Fulano', 'Brasileiro') 
    autor2 = Autor('Ciclano', 'Brasileiro')
    return [autor1, autor2]
    
#livro
def criar_livro(autores):
    return Livro('Python para iniciantes', 'Editora A', 'Tecnologia', autores) 


#usuario
def criar_usuario():
    return Usuario('Fulano', '123456789', 'Brasileiro') 

#exemplar
def criar_exemplares():
    exemplar1 = Exemplar("1", "Python para iniciantes", "disponível", 2)
    exemplar2 = Exemplar("2", "Python para iniciantes", "disponível", 2)
    return [exemplar1, exemplar2]

# emprestimo
def registrar_emprestimo(usuario, exemplar):
    data_emprestimo = datetime.strptime('01/01/2021', '%d/%m/%Y').date()
    data_devolucao = datetime.strptime('01/02/2021', '%d/%m/%Y').date()
    emprestimo = Emprestimo(data_emprestimo, data_devolucao, usuario, exemplar, False)
    return emprestimo

try:
    # chamando a função p/ criar autor
    autores = criar_autores()
    print('\n--- CRIANDO AUTOR ----')
    for autor in autores:
        print(autor)

    # livro
    livro = criar_livro(autores)
    print('\n--- CRIANDO LIVRO ----')
    print(livro)

    # usuário
    usuario = criar_usuario()
    print('\n--- CRIANDO USUARIO ----')
    print(usuario)

    # exemplar
    exemplares = criar_exemplares
    print('\n--- CRIANDO EXEMPLAR ----')
    for exemplar in exemplares:
        print(exemplar)

    # associar livro ao exemplar
    print('\n--- ASSOCIANDO LIVRO AO EXEMPLAR ----')
    for exemplar in exemplares:
        livro.adicionar_exemplar(exemplar)
    print(livro)

    # empréstimo
    emprestimo = registrar_emprestimo(usuario, exemplar)
    print('\n--- CRIANDO EMPRESTIMO ----')
    print(emprestimo)


   
except Exception as e:
    print(e)