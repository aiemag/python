#!/usr/bin/python3

def makeClass1():
    print("##### normal case to make class #####")

    class Foo():
        v1 = 1

        def show_v1(self):
            print('v1 : ',self.v1)
    

    def test(self):
        print('test text')

    Foo.test = test


    print(Foo)
    print(Foo().show_v1())
    print(Foo().test())

    print("\n")


def makeClass2():
    print("##### using type keyword to make class #####")

    def show_v1(self):
        print('v1 : ',self.v1)

    Foo = type('Foo', (), {'v1':1, 'show_v1': show_v1})
    
    def test(self):
        print('test text')

    Foo.test = test

    print(Foo)
    print(Foo().show_v1())
    print(Foo().test())

    print("\n")


def main():
    makeClass1()
    makeClass2()


if __name__ == "__main__":
    main()
