def algo():
    raise Exception('exceção')
    print('depois do raise')


def algo2():
    try:
        algo()
    except Exception:
        print('Eu peguei uma exceção')
        print('Executado após a exceção')


algo2()


def divisao(divisor):
    try:
        if divisor == 13:
            raise ValueError('13 não é legal')
        return 10 / divisor
    except ZeroDivisionError:
        return 'Divisão por zero'
    except TypeError:
        return 'Entre com um valor numérico'
    except ValueError:
        return 'Não utilize o número 13'


print('\n\n')

print(divisao(0))
print(divisao('text'))
print(divisao(13))

print('\n\n')

try:
    raise ValueError('este é um argumento')
except ValueError as e:
    print('Os argumentos da exceção foram: ', e.args)
finally:
    print('isso sempre será executado')
