d = dict()
d['anderson'] = 28
d['joao'] = 20
print(d)

d = {'anderson': 28, 'joao': 20}
print(d)

print(d.get('anderson'))
print(d.get('maria'))
print(d.keys())  # pode ser utilizado o for para percorrer esses elementos
print(d.values())  # pode ser utilizado o for para percorrer esses elementos
print(d.items())  # retorna uma lista

print('\n\n')

# dicionários não garantem a ordem
d = {'anderson': 28, 'joao': 20}
for nome, idade in d.items():
    print(nome, idade)

print('\n\n')


class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor


obj = MinhaClasse(20)
d = {}
d[obj] = 'anderson'
obj2 = MinhaClasse(28)
d[obj2] = 'joao'

print(d[obj])
print(d[obj2])

print('\n\n')

# listas são mutáveis
lista = [1, 2, 3, 'anderson']
print(lista[-1])
print(lista[0:2])
lista.append(10)
print(lista)
print(lista.count('anderson'))
print(help(list))

print('\n\n')

# conjuntos não permitem elementos repetidos, não garantem a ordem
c = set()
c.add(10)
c.add(20)
c.add(10)
c.add(20)
print(c)
print(help(set))
