#!/usr/bin/python3

import threading

def worker(param):
    print("name : %s, aregument : %s" % (threading.currentThread().getName(), param))


def main():
    for i in range(5):
        t = threading.Thread(target=worker, name="thread %i" % i, args=(i,))
        t.start()


if __name__ == "__main__":
    main()
