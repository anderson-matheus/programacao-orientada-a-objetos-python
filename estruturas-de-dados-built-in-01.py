from collections import namedtuple


class MinhaClasse:
    pass


obj = MinhaClasse()
obj.x = 140

print(obj.x)

# tuplas são imutáveis
# listas são mutáveis

t = (1, 'anderson', 3.14)
t = 'anderson', 1, 3.14
nome, idade, pi = t
print(nome)
print(idade)
print(pi)

t = (1, 2, 3)
print(t[0])
print(t[1])
print(t[1:3])

Estoque = namedtuple('Estoque', 'produtos')
Estoque = namedtuple('Estoque', 'x y z')

estoque = Estoque(10, 20, 30)
print(estoque.x)
print(estoque.y)
print(estoque.z)
