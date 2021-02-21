#!/usr/bin/python3

from functools import reduce

def test_reduce1():
    rst = reduce(lambda x, y: x+y, range(1,11))
    print(rst)


def test_reduce2():
    rst = reduce(lambda x, y: x+y, range(1,11), 10)
    print(rst)


def test_reduce3():
    rst = reduce(lambda x, y: x if x > y else y, range(1,11))
    print(rst)


def main():
    test_reduce1()   
    test_reduce2()   
    test_reduce3()   


if __name__ == "__main__":
    main()
