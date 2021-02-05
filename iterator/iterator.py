#!/usr/bin/python3

def main():
    x = [1, 2, 3]

    print('\ntest 1')
    x_iter = iter(x)
    for value in x_iter:
        print(value)


    print('\ntest 2')
    x_iter = iter(x)
    for i in range(4):
        print(next(x_iter)) 



if __name__ == "__main__":
    main()
