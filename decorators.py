'''
Decorator
    É uma função que recebe outra função como parâmetro,
    gera uma nova função que adiciona algumas funcionalidades á função
    original e retorna essa nova função
'''


def modificar(funcao):
    def somar_pares(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return a - b
    return somar_pares


@modificar
def somar(a, b):
    return a + b


print(somar(3, 3))


def meu_decarator(funcao):
    def imprime_algo():
        print('eu não sei somar')
    return imprime_algo


@meu_decarator
def imprime():
    print('eu sei somar')


# imprime = meu_gerador(imprime)

imprime()
