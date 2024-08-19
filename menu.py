from classes.livro import Livro
from classes.autor import Autor
from classes.emprestimo import Emprestimo
from classes.exemplar import Exemplar
from classes.item_biblioteca import ItemBiblioteca
from classes.pessoa import Pessoa
from classes.usuario import Usuario

livros = []

def criar_livro():
    print("\n--- Adicionar Livro ---")

    titulo = input("Digite o título do livro: ")
    editora = input("Digite a editora do livro: ")

    generos = input("Digite os gêneros do livro (separados por vírgula): ")
    generos = [genero.strip() for genero in generos.split(',')]  # Converte a string em uma lista de gêneros

    autores = []
    autores_input = input("Digite os autores do livro (nomes separados por vírgula): ")
    autores_nomes = [nome.strip() for nome in autores_input.split(',')]

    for nome in autores_nomes:
        nacionalidade = input(f"Digite a nacionalidade do autor {nome}: ")
        autor = Autor(nome, nacionalidade)
        autores.append(autor)

    exemplares = []
    adicionar_exemplares = input("Deseja adicionar exemplares agora? (s/n): ").strip().lower()

    while adicionar_exemplares == 's':
        id = input("Digite o identificador do exemplar: ")
        exemplar = Exemplar(id, titulo, estado="disponível", max_renovacoes=2)
        exemplares.append(exemplar)
        adicionar_exemplares = input("Deseja adicionar mais exemplares? (s/n): ").strip().lower()

    num_maximo_renovacoes = input(
        "Digite o número máximo de renovações permitido (ou deixe em branco para sem limite): ")
    num_maximo_renovacoes = int(num_maximo_renovacoes) if num_maximo_renovacoes else None

    # Criando uma instância de Livro
    livro = Livro(titulo, editora, generos, autores, exemplares, num_maximo_renovacoes)

    # Adicionando o livro à coleção de livros
    livros.append(livro)

    print(f'Livro "{livro.titulo}" adicionado com sucesso!')


def verificar_disponibilidade():
    titulo = input("Digite o título do livro para verificar sua disponibilidade: ")
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():  # Compara ignorando maiúsculas e minúsculas
            if livro.verificar_disponibilidade():
                print(f"O livro '{titulo}' está disponível para empréstimo.")
            else:
                print(f"Todos os exemplares do livro '{titulo}' estão emprestados.")
            return
    print("Livro não encontrado.")


def registrar_emprestimo():
    # Implementar a lógica de registro de empréstimo
    pass

def devolver_exemplar():
    # Implementar a lógica de devolução de exemplar
    pass

def renovar_emprestimo():
    # Implementar a lógica de renovação de empréstimo
    pass

def criar_usuario():
    # Implementar a lógica de criação de usuário
    pass

# Menu principal
def menu_principal():
    while True:
        print("\n--- Sistema da Biblioteca ---")
        print("1. Adicionar Livro\n"
              "2. Verificar Disponibilidade\n"
              "3. Registrar Empréstimo\n"
              "4. Devolver Exemplar\n"
              "5. Renovar Empréstimo\n"
              "6. Criar Usuário\n"
              "7. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")
            continue

        if opcao == 1:
            criar_livro()

        elif opcao == 2:
            verificar_disponibilidade()

        elif opcao == 3:
            registrar_emprestimo()

        elif opcao == 4:
            devolver_exemplar()

        elif opcao == 5:
            renovar_emprestimo()

        elif opcao == 6:
            criar_usuario()

        elif opcao == 7:
            print('Saindo...')
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o menu principal
if __name__ == "__main__":
    menu_principal()
