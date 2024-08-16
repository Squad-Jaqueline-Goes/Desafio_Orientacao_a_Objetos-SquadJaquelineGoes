class Livro:
    def __init__(self, titulo, exemplares):
        self.titulo = titulo
        self.exemplares = exemplares

    def esta_disponivel(self):
        return any(exemplar.estado == "disponível" for exemplar in self.exemplares)


        exemplar1 = Exemplar(estado="emprestado")
        exemplar2 = Exemplar(estado="disponível")

        livro = Livro(titulo="Título do Livro", exemplares=[exemplar1, exemplar2])
        
if livro.esta_disponivel():
    print("O livro está disponível.")
else:
    print("O livro não está disponível.")
