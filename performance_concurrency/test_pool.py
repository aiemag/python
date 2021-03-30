from multiprocessing import Pool, pool

import os
import time

data = []
for i in range(0,10000000):
    data.append(i)


def do_single_processing(data):
    result = []
    for i in range(0, len(data)):
        result.append(data[i]*data[i])

    return result


def do_multi_processing(x):
    return x*x


if __name__ == "__main__":

    start = time.time()
    result = do_single_processing(data)
    print("result : ",sum(result))
    print("single elapsed time : ",(time.time() - start))

    start = time.time()
    with Pool(processes=4) as pool:
        result = pool.map(do_multi_processing, data)
    print("result : ",sum(result))
    print("pool elapsed time : ",(time.time() - start))

