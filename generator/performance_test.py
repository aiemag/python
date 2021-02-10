#!/usr/bin/python3

import time

def gen1(count):
    g_list = []
    for i in range(count):
        g_list.append(i)     

    return g_list


def gen2(count):
    for i in range(count):
        yield i


def test_more(f):

    def inner(*args, **kwargs):

        count = 10
        init_t, process_t, total = 0, 0, 0

        for i in range(count):
            init_t_, process_t_, total = f(*args, **kwargs)
            init_t += init_t_
            process_t += process_t_

        print("%s average - init time : %s, process time : %s, total : %s\n" % 
            (f.__name__, init_t/count, process_t/count, total/count))

    return inner


@test_more
def test1():

    t1 = time.clock()
    g_ret = gen1(1000000)
    t2 = time.clock()
    init_t = t2 - t1

    t1 = time.clock()
    total = 0
    for v in g_ret:
        total += v
    t2 = time.clock()
    process_t = t2 - t1

    return init_t, process_t, total


@test_more
def test2():

    t1 = time.clock()
    g_ret = gen2(1000000)
    t2 = time.clock()
    init_t = t2 - t1

    t1 = time.clock()
    total = 0
    for v in g_ret:
        total += v
    t2 = time.clock()
    process_t = t2 - t1

    return init_t, process_t, total


if __name__ == "__main__":
    test1()
    test2()
