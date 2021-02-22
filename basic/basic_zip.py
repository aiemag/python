#!/usr/bin/python3

def main():
    key_list = ['a', 'b', 'c']
    value_list = [1, 2, 3]
    my_dic = {}

    for k, v in zip(key_list, value_list):
        my_dic[k] = v

    print(type(my_dic))
    print(my_dic)


if __name__ == "__main__":
    main()
