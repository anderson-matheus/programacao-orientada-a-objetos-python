# F = F(n - 1) + F(n - 2)


class fib:
    """
    Método para calcular o fibonacci

    >>> f.calculo_fib(10)
    55
    >>> f.calculo_fib(1)
    1
    >>> f.calculo_fib(-1)
    Traceback (most recent call last):
    ...
    ValueError: Não tem que ser maior que zero!!!
    """

    def calculo_fib(self, n):
        if n < 0:
            raise ValueError('Não tem que ser maior que zero!!!')

        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'f': fib()})
