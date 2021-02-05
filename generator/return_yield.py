#!/usr/bin/python3


def gen():
    yield 1
    yield 2
    yield 3


def normal():
    return 1
    return 2
    return 3


def main():
    print("gen()")
    print(gen())
    print("normal()")
    print(normal())

    print("gen() print by for")
    for g in gen():
        print(g)

    print("normal() print by for")
    for n in normal():
        print(n)



if __name__ == "__main__":
    main()
