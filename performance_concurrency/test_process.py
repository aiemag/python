#!/usr/bin/python3

import pandas as pd
import time
import concurrent.futures
import multiprocessing
from functools import reduce

df = None

def make_data():
    global df
    df = pd.DataFrame(columns=['NO', 'A', 'B'])

    no_list = []
    a_list = []
    b_list = []

    for i in range(1000000):
        no_list.append(i)
        a_list.append(i+1)
        b_list.append(i+2)

    df['NO'] = no_list
    df['A'] = a_list
    df['B'] = b_list

    df.to_csv("./testset.csv", sep=",", index=False)


def load_data():
    global df
    df = pd.read_csv("./testset.csv")


def process1():
    global df

    #df = df[df['A']%2==0]    
    result = df['A'].sum()
    print("result : ", result)


def worker(q, data):
    q.put(sum(data))


def process2():
    q = multiprocessing.Queue()

    data = df['A'].tolist()

    p1 = multiprocessing.Process(target=worker, args=(q,data[:250000]))
    p1.start()
    p2 = multiprocessing.Process(target=worker, args=(q,data[250000:500000]))
    p2.start()
    p3 = multiprocessing.Process(target=worker, args=(q,data[500000:750000]))
    p3.start()
    p4 = multiprocessing.Process(target=worker, args=(q,data[750000:]))
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


def main():

    #make_data() 
    load_data()

    stime = time.time()
    process1()
    print("single elapsed time : ",time.time() - stime)

    stime = time.time()
    process2()
    print("multi elapsed time : ",time.time() - stime)


if __name__ == "__main__":
    main()
