
import debug
import logging


class Usuario:

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.dict_user = {'1': 'Thomas',
                          '2': 'Marcos',
                          '3': 'José',
                          '4': 'QualquerNome'}
        formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename='usuario.log',
                            level=logging.DEBUG, filemode='w',
                            format=formato, datefmt="%d/%m/%Y %I:%M:%S %p")
        self.logger = logging.getLogger(__file__)

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        self.logger.info('Senha alterada')

    def autentica(self, usuario, senha):
        if self.usuario != usuario or self.senha != senha:
            self.logger.warning('Tentativa de acesso inválido')
            return False
        return True

    def get_usuario_by_id(self, usuario_id):
        user = self.dict_user.get(usuario_id, None)
        if user is None:
            self.logger.error('Usuário não existe: usuario_id={}'.format(
                usuario_id
            ))
            return None
        return user

    def abrir_arquivo_usuario(self):
        try:
            open('/path/to/does/not/exist', 'rb')
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            self.logger.exception('Error:')

    def algoritmo_complex(self, items):
        for i, item in enumerate(items):
            # faz algum complexo algoritmo_complex
            self.logger.debug('{0} iterator, item={1}'.format(
                i, item
            ))


if __name__ == '__main__':
    user = Usuario("Thomas", "1234")
    user.alterar_senha("123456")
    user.autentica("Thomas", "123589")
    user.get_usuario_by_id("25")
    user.abrir_arquivo_usuario()
    user.algoritmo_complex([1, 2, 3, 4])
    debug.execute()
