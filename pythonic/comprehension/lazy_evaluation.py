#!/usr/bin/python3

def print_n_return(num):
    print('*')

    return num


def main():

    print("list comprehension")
    list_iterator = [print_n_return(x) for x in range(5)]
    for v in list_iterator:
        print(v)


    print("list generator expression")
    generator_iterator = (print_n_return(x) for x in range(5))
    for v in generator_iterator:
        print(v)


if __name__ == "__main__":
    main()
