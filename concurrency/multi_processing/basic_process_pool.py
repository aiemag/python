#!/usr/bin/python3

import multiprocessing

def print_initial_msg():
    print("Start process : %s" % multiprocessing.current_process().name)


def worker(data):
    print("worker process : %s" % multiprocessing.current_process().name)
    return data*2


def main():
    pool = multiprocessing.Pool(processes=2, initializer=print_initial_msg)
    data_list = range(10)
    result = pool.map(worker, data_list)

    pool.close()
    pool.join()

    print("Result : %s" % result)


if __name__ == "__main__":
    main()
