#!/usr/bin/python3

def gen():
    value = 1
        
    while True:
         value = yield value


def main():
    g = gen()

    print(next(g))
    print(g.send(3))
    print(g.send(5))
    print(next(g))


if __name__ == "__main__":
    main()
