class P():
    pass


p = P()
print(P.__mro__)
print(P.mro())


class Veiculo():
    pass


class Carro(Veiculo):
    pass


class Trem(Veiculo):
    pass


print(Veiculo.__mro__)
print(Carro.__mro__)


class CarroTrem(Carro, Trem):
    pass


print(CarroTrem.__mro__)


class Veiculo():
    def __init__(self):
        pass


class Carro(Veiculo):
    def __init__(self):
        super(Carro, self).__init__()


print(Carro.__mro__)
