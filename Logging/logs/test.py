from logger import logging

def add(a,b):
    logging.debug('addition is taking place')
    return a+b

logging.debug('Addition complete')
add(23,5)