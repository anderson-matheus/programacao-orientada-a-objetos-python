class A:
    def fazer_algo(self):
        pass

    def outro_metodo(self):
        pass

    def algum_metodo(self, nome):
        return nome


class B:
    def __init__(self):
        self.a = A()

    def fazer_algo(self):
        # delega para self.a
        return self.a.fazer_algo

    def outro_metodo(self):
        # delega para self.a
        return self.a.outro_metodo

    def __getattr__(self, nome):
        return getattr(self.a, nome)


b = B()
b.fazer_algo()  # chame B.fazer_Algo() (existe em B
# chama B.__getattr__('algum_metodo') e delega para A.algum_metodo
print(b.algum_metodo('python'))
