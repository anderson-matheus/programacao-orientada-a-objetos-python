from database import BancoDeDados

if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

    banco.inserir_cliente('Lucas Henry Freitas',
                          '123456',
                          '69824857818',
                          'llucashenryfreitas@djapan.com.br')
    banco.inserir_cliente('Enrico Raul Pedro Barbosa',
                          '123456',
                          '25909656210',
                          'eenricoraulpedrobarbosa@dc4.com.br')
    banco.inserir_cliente('Joaquim Guilherme Rodrigues',
                          '123456',
                          '91436687470',
                          'eenricoraulpedrobarbosa@dc4.com.br')

    banco.buscar_cliente('259096asdasd56210')
    login = banco.login('Lucas Henry Freitas', '123456')
    print(login)

    cpf = '69824857818'
    remover = banco.remover_cliente(cpf)

    email = 'eenricoraulpedrobarbosa@dc4.com.br'
    buscar = banco.buscar_email(email)
    banco.desconecta()
