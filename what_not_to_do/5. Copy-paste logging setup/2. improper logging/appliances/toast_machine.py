import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def turn_on():
    logger.debug('Supplying electricity to toast machine microcontrollers')
    # code
    logger.info('Toast machine is on!')
