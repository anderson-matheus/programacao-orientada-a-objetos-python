def funcao(*args):
    print(args)


funcao(1, 2, 3, 'anderson')


# keyword arguments
def funcao(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


funcao(nome='anderson', idade=28, linguagem='python')
