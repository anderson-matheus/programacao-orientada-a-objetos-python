for i in 'anderson':
    print(i)

lista = [i * 2 for i in range(1, 11)]
print(lista)

# Fibonacci: 1, 1, 2, 3, 5, 8, 13, ...


class Fibonacci:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.x, self.y = 1, 1
        return self

    def __next__(self):
        fib = self.x
        if fib > self.max:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return fib


fib = Fibonacci(100)

for i in fib:
    print(i, end=' ')
