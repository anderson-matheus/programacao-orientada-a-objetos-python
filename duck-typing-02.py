class Pato:
    def quack(self):
        return 'Quack, quack'


class Pessoa:
    def quack(self):
        return 'Eu faço quack igual a um pato'


'''
# Isso não é pythonico
def fazer_quack(obj):
    if isinstance(obj, Pato):
        print(obj.quack())
    else:
        print('Isso tem que ser um pato')
'''

'''
def fazer_quack(obj):
    # LBYL - NÃO pythonico
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            print(obj.quack())
'''


'''
# EAFP - Easier to ask for forgiveness than permission
É pythonico
'''


def fazer_quack(obj):
    try:
        print(obj.quack())
    except AttributeError as e:
        print(e)


pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
