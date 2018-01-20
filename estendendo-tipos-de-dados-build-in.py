print(1 + 2)
print((1).__add__(2))


class MeuInt(int):
    def __add__(self, num):
        return 0


a = MeuInt(1)
print(a + 2)
print(dir(list))
print(help(list.append))

lista = [1, 2, 3, 4]
lista.append(5)
print(lista)


class MinhaLista(list):
    def append(self, *args):
        self.extend(args)


lista = MinhaLista()
lista.append(1)
lista.append(2, 3, 4, 5, 6, 7)
print(lista)


class MyList(list):
    def sort(self):
        return 'opa, você quer ordernar?'


lista = [10, 50, 20]
lista.sort()
print(lista)

lista = MyList()
print(lista.sort())
