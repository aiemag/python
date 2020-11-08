#!/usr/bin/python3

def decorator(func):

    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper


@decorator
def test1():
    print("test function")


def test2():
    print("test function")


def main():
    test1() # using notation
    print()
    decorator(test2)() #not using notation 

if __name__ == "__main__":
    main()
    
