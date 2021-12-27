import logging
import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(*args, sep="\n")
        for key, value in kwargs.items():
            print(key, value)
        func(*args, **kwargs)
        end = time.time()
        print(f"Time of function running {(end - start)} seconds")

    return wrapper


@my_decorator
def my_func(first, second, third, **options):
    if options.get("action") == "sum":
        print(f"The sum is: {first + second + third}")

    if options.get("action") == "minimal":
        print(f"Minimal number is: {min(first, second, third)}")

    a = [i for i in range(10000000)]
    return a


my_func(8, 6, 3, action="minimal", something="two")
