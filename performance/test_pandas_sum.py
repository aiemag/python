#!/usr/bin/python3

import pandas as pd
import time
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

    df = df[df['A']%2==0]    
    result = df['A'].sum()
    print("result : ", result)


g_result = 0

def worker(x):
    global g_result
    g_result += x 


def process2():

    pool = multiprocessing.Pool(processes=2) 
    result = pool.map(worker, df['A'].tolist())

    print("g_result : ", g_result)


def main():
    stime = time.time()

    #make_data() 
    load_data()
    process1()
    #process2()

    print("Elapsed time : ",time.time() - stime)


if __name__ == "__main__":
    main()
