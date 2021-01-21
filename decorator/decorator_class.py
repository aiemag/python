#!/usr/bin/python3

from functools import update_wrapper

class DecoratorClass:

    def __init__(self, f):
        self.func = f
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        print("before")
        ret = self.func(*args, **kwargs)
        print("after")

        return ret
        

@DecoratorClass
def test1(value):
    print("test1 :",value)


def test2(value):
    print("test2 :",value)


def main():
    test1(7)
    DecoratorClass(test2)(5)


if __name__ == "__main__":
    main()
