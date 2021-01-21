#!/usr/bin/python3

import time
from functools import wraps

def decorator1(func):

    def wrapper():
        ret = func()
        print("decorator1() func name : %s" % func.__name__)
        
        return ret

    return wrapper


def decorator2(func):

    def wrapper():
        start = time.time()
        ret = func()
        end = time.time()
        print("%s" % str(end - start))
        print("decorator2() func name : %s" % func.__name__)

        return ret

    return wrapper


def decorator3(func):

    @wraps(func)
    def wrapper():
        ret = func()
        print("decorator3 is called.")
        print("decorator3() func name : %s" % func.__name__)

        return ret

    return wrapper


@decorator1
@decorator2
@decorator3
def test():
    time.sleep(3)


def main():
    test()


if __name__ == "__main__":
    main()
