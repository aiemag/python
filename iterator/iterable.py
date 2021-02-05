#!/usr/bin/python3

def main():
    x = [1, 2, 3]
    x_iter = iter(x)
    print("x type : %s" % type(x))
    print("x_iter type : %s" % type(x_iter))
    print("x_iter next : %s" % next(x_iter))
    print("x next : %s" % next(x))


if __name__ == "__main__":
    main()
