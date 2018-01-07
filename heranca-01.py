# -*- coding: utf-8 -*-
class MinhaClasse(object):
    pass


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CPF = CPF


class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.CNPJ = CNPJ


print('Pessoa')
p1 = Pessoa('anderson', 28)
print(p1.nome)
print(p1.idade)
print('\n\n')

print('Pessoa Física')
p_fisica = PessoaFisica('44841766880', 'anderson', 28)
print(p_fisica.CPF)
print(p_fisica.nome)
print(p_fisica.idade)
print('\n\n')

print('Pessoa Jurídica')
p_juridica = PessoaJuridica('39492365000116', 'anderson', 28)
print(p_juridica.CNPJ)
print(p_juridica.nome)
print(p_juridica.idade)
print('\n\n')
