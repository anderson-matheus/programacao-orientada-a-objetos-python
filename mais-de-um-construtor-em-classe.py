class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # construtor alternativo
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)  # retornado a instância final


p1 = Pessoa('Anderson')
print(p1.nome)

p2 = Pessoa.outro_construtor('Matheus')
print(p2.nome)
