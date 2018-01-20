# # def algo():
# #     print('POO com Python')
# #     raise Exception('Lançando exceção')
# #     print('depois da exceção')
# #     return 'sucesso'
#
#
# algo()


def algo2():
    raise Exception('Exceção em algo2')


def algo3():
    print('antes da chamada da função')
    algo2()
    print('depois da chamada da função')


algo3()
