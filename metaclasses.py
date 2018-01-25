class MinhaClasse(object):
    var = True


MinhasClasses = type('MinhaClasse', (), {'var': True})
print(MinhasClasses)

obj = MinhaClasse()
print(obj.var)

a = 10
print(a.__class__)
str = 'anderson'
print(a.__class__.__class__)


class MinhaMetaClasse(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print('clsname: ', clsname)
        print('superclasses: ', superclasses)
        print('atributos: ', attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class Pai:
    pass


class Filha(Pai, metaclass=MinhaMetaClasse):
    pass


obj = Filha()
print(obj.__class__)
print(obj.__class__.__class__)
