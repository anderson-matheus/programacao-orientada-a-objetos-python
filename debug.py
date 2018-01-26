import logging


def execute():
    formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='python-log.log',
                        level=logging.DEBUG, filemode='w',
                        format=formato, datefmt="%d/%m/%Y %I:%M:%S %p")
    logger = logging.getLogger(__file__)

    logger.info('Mensagem informativa')
    logger.debug('Mensagem de debug')
    logger.error('Um erro aconteceu')


if __name__ == '__main__':
    execute()
