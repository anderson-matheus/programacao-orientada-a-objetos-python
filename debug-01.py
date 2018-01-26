import logging


'''
Níveis de logging
    - INFO
    - DEBUG
    - WARNING
    - ERROR
    - CRITICAL
'''
formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='python-log.log',
                    level=logging.DEBUG, filemode='w',
                    format=formato)
# logger = logging.getLogger(__name__)
logger = logging.getLogger(__file__)

logger.info('Mensagem informativa')
logger.debug('Mensagem de debug')
logger.error('Um erro aconteceu')
