# -*- coding: utf-8 -*-
class Funcionario:
    def __init__(self, nome, salario, CPF):
        self.nome = nome
        self.salario = salario
        self.CPF = CPF
        # self.__x = x  # __ siginifica que o atributo é privado

    def get_bonificacao(self):
        return self.salario * 0.20


class Gerente(Funcionario):
    def __init__(self, nome, salario, CPF, senha):
        super().__init__(nome, salario, CPF)
        self.senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00


g = Gerente('Anderson', 1500.00, '44841766880', 123456)
print(g.nome)
print(g.get_bonificacao())
print(g.senha)
