#!/usr/bin/python3


def print_comprehension():
    # list comprehension
    o_list = [1, 2, 3]
    c_list = [x*x for x in o_list]

    print("list comprehension output : ", c_list)

    # dic comprehension
    o_dic_key = ["a", "b", "c"]
    o_dic_value = [1, 2, 3]
    c_dic = {k:v for k, v in zip(o_dic_key, o_dic_value)}

    print("dictionary comprehension output : ", c_dic)


def print_generator_expression():
    # list generator expression
    o_list = [1, 2, 3]
    g_exp = (x*x for x in o_list)

    print("list generator expression output : ")
    for v in g_exp:
        print(v)


def main():
    print_comprehension()
    print_generator_expression()


if __name__ == "__main__":
    main()
