from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print('au au au')


class Gato(Animal):
    def falar(self):
        print('miau miau')


class Fabrica(object):
    def produzir_som(self, object_type):
        return eval(object_type)().falar()


if __name__ == '__main__':
    f = Fabrica()
    f.produzir_som('Gato')
    f.produzir_som('Cachorro')
