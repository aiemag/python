#!/usr/bin/python3


def closure(x):
    
    def inner(y):
        return x+y

    return inner


def main():
    ret = closure(10)
    print(ret(5))


if __name__ == "__main__":
    main()
