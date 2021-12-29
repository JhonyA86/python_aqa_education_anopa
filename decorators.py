import logging
import time


class IncorrectInputValueType(Exception):
    def __init__(self):
        self.message = "Incorrect input value, please enter only digits"

    def __str__(self):
        return self.message


class NegativeValueError(Exception):
    def __init__(self):
        self.message = "Negative number, please enter correct"

    def __str__(self):
        return self.message


logging.basicConfig(handlers=[
    logging.FileHandler("myfunc.log"),
    logging.StreamHandler()
], format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def my_decorator(func):
    def wrapper(*args, **kwargs):
        for a in args:
            logging.info(f" Argument {a},type {type(a)})")
        for key, value in kwargs.items():
            logging.info(f" Argument {key}, {value}, {type(value)}")
        logging.info("Start function")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        logging.info(f"Time of function running {(end - start)} seconds")

    return wrapper


@my_decorator
def my_func(first, second, third, **options):
    try:
        if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
            raise IncorrectInputValueType
        if first < 0 or second < 0 or third < 0:
            raise NegativeValueError
    except IncorrectInputValueType:
        logging.error("Incorrect input value, please enter only digits")
    except NegativeValueError:
        logging.error("Negative number, please enter correct")
    else:
        if options.get("action") == "sum":
            print(f"The sum is: {first + second + third}")
        if options.get("action") == "minimal":
            print(f"Minimal number is: {min(first, second, third)}")
        if options.get("more") == "iteration":
            a = [i for i in range(10000000)]
            return a


my_func(7, 9, 4, action="minimal", more="iteration")
