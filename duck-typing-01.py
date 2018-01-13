class Livro():
    def __init__(self, titulo, lancamento, autor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.autor = autor


class Filme():
    def __init__(self, titulo, lancamento, diretor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.diretor = diretor


def imprimir(midia):
    print(midia.titulo, midia.lancamento)
