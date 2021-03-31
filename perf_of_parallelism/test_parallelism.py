#!/usr/bin/python3

import pandas as pd
import time
import concurrent.futures
import multiprocessing
import threading
from functools import reduce

SLEEP_VAL = 0.0001

df = None
data = None

def make_data():
    global df
    df = pd.DataFrame(columns=['NO', 'A', 'B'])

    no_list = []
    a_list = []
    b_list = []

    for i in range(100000):
        no_list.append(i)
        a_list.append(i+1)
        b_list.append(i+2)

    df['NO'] = no_list
    df['A'] = a_list
    df['B'] = b_list

    df.to_csv("./testset.csv", sep=",", index=False)


def load_data():
    global df, data
    df = pd.read_csv("./testset.csv")
    data = df['A'].tolist()


def process1():
    # 1. fastest than multi processing
    #result = df['A'].sum() 
    
    # 2. faster than multi processing
    #result = sum(data)

    # 3. slower than multi processing
    result = 0
    for i in range(0, len(data)):
        time.sleep(SLEEP_VAL)
        result += data[i] 
    print("result : ", result)


def worker_for_process(q, data, p_idx):
    print('worker for process : ',p_idx)

    result = 0
    for i in range(0, len(data)):
        time.sleep(SLEEP_VAL)
        result += data[i] 
    q.put(result)
    #q.put(sum(data))


def process2():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=worker_for_process, args=(q,data[:25000], 0))
    p1.start()
    p2 = multiprocessing.Process(target=worker_for_process, args=(q,data[25000:50000], 1))
    p2.start()
    p3 = multiprocessing.Process(target=worker_for_process, args=(q,data[50000:75000], 2))
    p3.start()
    p4 = multiprocessing.Process(target=worker_for_process, args=(q,data[75000:], 3))
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    result = q.get()
    result += q.get()
    result += q.get()
    result += q.get()
    print("result : ", result)


result_list = [0,0,0,0] 
def worker_for_thread(data, t_idx):
    print('worker for thread : ',t_idx)

    global result_list

    for i in range(0, len(data)):
        time.sleep(SLEEP_VAL)
        result_list[t_idx] += data[i] 
 

def process3():
    t1 = threading.Thread(target=worker_for_thread, args=(data[:25000],0, ))
    t1.start()
    t2 = threading.Thread(target=worker_for_thread, args=(data[25000:50000],1, ))
    t2.start()
    t3 = threading.Thread(target=worker_for_thread, args=(data[50000:75000],2, ))
    t3.start()
    t4 = threading.Thread(target=worker_for_thread, args=(data[75000:],3, ))
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("result : ", sum(result_list))



def main():

    #make_data() 
    load_data()

    stime = time.time()
    process1()
    print("1 core - processing elapsed time : ",time.time() - stime)

    stime = time.time()
    process2()
    print("4 core - multi processing elapsed time : ",time.time() - stime)

    stime = time.time()
    process3()
    print("4 core - multi threading elapsed time : ",time.time() - stime)


if __name__ == "__main__":
    main()
