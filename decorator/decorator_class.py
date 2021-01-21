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
def test(value):
    print("test :",value)


def main():
    test(7)


if __name__ == "__main__":
    main()
