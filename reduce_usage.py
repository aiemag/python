#!/usr/bin/python3

from functools import reduce

def test_reduce():
    rst = reduce(lambda x, y:x+y, range(1,11))
    print(rst)


def main():
    test_reduce()   


if __name__ == "__main__":
    main()
