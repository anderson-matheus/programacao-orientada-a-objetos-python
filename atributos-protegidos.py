# 1 underscore é um atributo privado (não interpretado pelo python)
# 2 underscores é um atributo protegido (interpretado pelo python)
# Atributos protegidos são muito utilizados em api's


class P:
    def __init__(self, x):
        self.__x = x


obj = P(10)
print(obj._P__x)
