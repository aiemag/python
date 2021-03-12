#!/usr/bin/python3

class A:
    var_common = 'A'

    def showCommon(self):
        print("common A")

    def showA(self):
        print("A")


class B:
    var_common = 'B'

    def showCommon(self):
        print("common B")

    def showB(self):
        print("B")

class C:
    def showC(self):
        print("C")
        self.showCommon()


# Mixin - Overriding 
def process1():
    print('\n##### Overriding #####')

    class Foo(B, A):
        pass

    foo = Foo()
    foo.showCommon()
    print(foo.var_common)


# Mixin - Polymorphism
def process2():
    print('\n##### Polymorphism #####')

    class Foo1(C, B):
        pass

    class Foo2(C, A):
        pass

    foo1 = Foo1()
    foo1.showC()

    foo2 = Foo2()
    foo2.showC()


# Mixin - Can't implement Mixin with single inheritance
def process3():
    print('\n##### Polymorphism #####')

    c = C(A)
    c.showC()


def main():
    process1()
    process2()
    process3()
    

if __name__ == "__main__":
    main()
