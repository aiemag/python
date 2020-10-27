#!/usr/bin/python3

def test_map1():
    a = ["1", "2", "3", "4"]
    b = list(map(int, a))
    print(b)


def test_map2():
    a = list(map(str, range(10)))
    print(a)


def test_map3():
    
    def convert(data):
        return int(data)

    a = ["1", "2", "3", "4"]
    b = map(convert, a)
    print(b)
    print(list(b))


def main():
    test_map1()
    test_map2()
    test_map3()


if __name__ == "__main__":
    main()
