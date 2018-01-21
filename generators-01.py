# Generators (geradores)
# Fibonacci: 1, 1, 2, 3, 5, 8 ...


def fib(maior):
    x, y = 1, 1
    while x < maior:
        yield x  # parecido com o return a diferença é que retorna um gerador
        x, y = y, x + y


gen = fib(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('\n\n')

gen = fib(10)
for i in gen:
    print(i)
