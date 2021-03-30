from multiprocessing import Pool, pool

import os
import time

data = []
for i in range(0,1000):
    #time.sleep(0.001)
    data.append(i)


def do_square(v):
    #time.sleep(0.001)
    return v*v

def do_multi_processing(data):
    return do_square(data)


def do_single_processing(data):
    rst = []
    for i in range(0, len(data)):
        rst.append(data[i]*data[i])


if __name__ == "__main__":

    start = time.time()
    do_single_processing(data)
    print("single elapsed time : ",(time.time() - start))

    start = time.time()
    with Pool(processes=8) as pool:
        pool.map(do_multi_processing, data)
    print("pool elapsed time : ",(time.time() - start))

