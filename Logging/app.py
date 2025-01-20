import logging

# logging configuration

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} and {b}: {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a}: {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b}: {result}")
    return result

def divide(a, b):
    if b == 0:
        logger.error("Division by zero error!")
        raise ValueError("Cannot divide by zero.")
    result = a / b
    logger.debug(f"Dividing {a} by {b}: {result}")
    return result

add(10,15)
subtract(15,10)
multiply(2,3)
divide(40,10)