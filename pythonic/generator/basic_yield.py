#!/usr/bin/python3


def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    v = 1

    while True:
        v = yield v
        print("-----------")
        print("v : ", v)


def main():
    print("test1")
    for g in gen1():
        print(g) 

    print("test2")
    g2 = gen2()
    print(next(g2))   
    print(g2.send(3))   
    print(g2.send(5))   
    print(next(g2))   

if __name__ == "__main__":
    main()
