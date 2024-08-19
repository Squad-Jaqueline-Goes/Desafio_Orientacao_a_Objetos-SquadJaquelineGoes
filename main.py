from classes.livro import Livro
from classes.autor import Autor
from classes.emprestimo import Emprestimo
from classes.exemplar import Exemplar
from classes.item_biblioteca import ItemBiblioteca
from classes.pessoa import Pessoa
from classes.usuario import Usuario

livros = []
usuarios = []


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
    print("\n--- Registrar Empréstimo ---")
    titulo = input(str("Digite o título do livro que deseja emprestar: "))
    usuario_nome = input("Digite o nome do usuário: ")

    usuario = next((u for u in usuarios if u.nome.lower() == usuario_nome.lower()), None)
    if not usuario:
        print("Usuário não encontrado.")
        return

    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            exemplares_disponiveis = [exemplar for exemplar in livro.exemplares if exemplar.estado == "disponível"]
            if exemplares_disponiveis:
                print("Exemplares disponíveis:")
                for exemplar in exemplares_disponiveis:
                    print(f"ID: {exemplar.id}")
                id_exemplar = input("Digite o ID do exemplar que deseja emprestar: ")
                exemplar = next((exemplar for exemplar in exemplares_disponiveis if exemplar.id == id_exemplar), None)
                if exemplar:
                    data_emprestimo = input("Digite a data de empréstimo (DD/MM/AAAA): ")
                    data_devolucao = input("Digite a data de devolução (DD/MM/AAAA): ")
                    emprestimo = Emprestimo(data_emprestimo, data_devolucao, exemplar, usuario, renovar_emprestimo())
                    emprestimo.registrar_emprestimo()
                    print(f"Empréstimo registrado com sucesso! Data de devolução: {data_devolucao}")
                else:
                    print("Exemplar não encontrado.")
            else:
                print("Todos os exemplares do livro estão emprestados.")
            return
    print("Livro não encontrado.")


def devolver_exemplar():
    print("\n--- Devolver Exemplar ---")
    id_exemplar = input("Digite o ID do exemplar que deseja devolver: ")

    for livro in livros:
        exemplar = next((exemplar for exemplar in livro.exemplares if exemplar.id == id_exemplar), None)
        if exemplar:
            emprestimo = exemplar.emprestimo_atual
            if emprestimo:
                emprestimo.registrar_devolucao()
                print(f"Exemplar {id_exemplar} devolvido com sucesso!")
                return
            else:
                print("Este exemplar não está atualmente emprestado.")
                return
    print("Exemplar não encontrado.")


def renovar_emprestimo():
    print("\n--- Renovar Empréstimo ---")
    id_exemplar = input("Digite o ID do exemplar que deseja renovar: ")

    for livro in livros:
        exemplar = next((exemplar for exemplar in livro.exemplares if exemplar.id == id_exemplar), None)
        if exemplar:
            emprestimo = exemplar.emprestimo_atual
            if emprestimo:
                if emprestimo.renovar_emprestimo():
                    print(f"Empréstimo do exemplar {id_exemplar} renovado com sucesso!")
                else:
                    print(f"O exemplar {id_exemplar} atingiu o limite máximo de renovações.")
                return
            else:
                print("Este exemplar não está atualmente emprestado.")
                return
    print("Exemplar não encontrado.")


def criar_usuario():
    print("\n--- Criar Usuário ---")
    nome = input("Digite o nome do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    nacionalidade = input("Digite a nacionalidade do usuário: ")

    usuario = Usuario(nome, telefone, nacionalidade)
    usuarios.append(usuario)

    print(f'Usuário "{nome}" criado com sucesso!')


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
