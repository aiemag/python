#!/usr/bin/python3

class A:
    v1 = 1

    def __init__(self):
        pass


    def print_v1(self):
        print(self.v1)
    

class B(A):
    
    def test(self):
        l2 = self.v1
        print(self.v1)
        print(l2)
        self.print_v1()
    

def main():
    b = B()
    b.test()


if __name__ == "__main__":
    main()
