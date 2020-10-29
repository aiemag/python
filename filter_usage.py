#!/usr/bin/python3

names = ["jack", "jay", "robert", "john"]

def test_filter1():

    def starts_with_j(x):
        return x.startswith('j')

    rst = filter(starts_with_j, names)
    print(list(rst))


def test_filter2():
    
    def starts_with(c):

        def func(x):
            return x.startswith(c)
 
        return func 

    rst = filter(starts_with('j'), names)
    print(list(rst))


def test_filter3():

    print(list(filter(lambda x: x.startswith('j'), names)))


def test_filter4():
    
    def starts_with_j(x):
        return x.startswith('j')

    # using list comprehension
    rst = [x for x in names if starts_with_j(x)]
    print(rst)


def main():
    test_filter1()
    test_filter2()
    test_filter3()
    test_filter4()


if __name__ == "__main__":
    main()
