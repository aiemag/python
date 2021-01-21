#!/usr/bin/python3

import time
from functools import wraps

def decorator1(func):

    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print("decorator1() func name : %s" % func.__name__)
        
        return ret

    return wrapper


def decorator2(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("%s" % str(end - start))
        print("decorator2() func name : %s" % func.__name__)

        return ret

    return wrapper


def decorator3(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print("decorator3 is called.")
        print("decorator3() func name : %s" % func.__name__)

        return ret

    return wrapper


@decorator1
@decorator2
@decorator3
def test(value):
    time.sleep(value)


def main():
    test(3)


if __name__ == "__main__":
    main()
