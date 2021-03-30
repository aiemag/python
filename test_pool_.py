from multiprocessing import Pool, cpu_count, pool, current_process

import os
import time

userlist = list()

for i in range(0, 1000000):
    userlist.append(i)
# userlist = [
#     123,
#     2123,
#     423,
#     532,
#     12,
#     435,
#     123,
#     45654,
#     23,
#     10,
#     2777,
#     5423,
#     4243,
#     214,
#     1233,
#     21223,
#     223,
# ]
sum = 0
# userlist = list()


def insertSample(left, right):
    print('debug : ', left, right)
    for i in range(left, right):
        pass
    #print('debug : ', left, right)
    #for i in range(left, right + 1):
        #print('print i ',i)
        # print("os id : " + str(current_process()) + " " + str(i) + " " + str(userlist[i]) + "\n")


#       print(str(os.getpid) + str(left) + " " + str(right) + " " + str(userlist[i]))
#   print(userlist[i])


#  print(userlist[i])

# print(sum + userlist[i])


def multiprocessSample(args):
    return insertSample(*args)


def startprocessing():
    np = 4
    #np = cpu_count()
    print(f"You have {np} cores")
    usersize = len(userlist) - 1

    indexlist = list()
    cpucount = np
    countindex, _ = divmod(usersize, cpucount)
    lastindex = countindex
    pivot = 0
    remainIndex = 0
    indexlist.append((pivot, countindex))
    while True:
        pivot = lastindex + 1
        lastindex = lastindex + countindex
        if lastindex < usersize:
            indexlist.append((pivot, lastindex))
        else:
            remainIndex = usersize - lastindex
            indexlist.append((pivot, lastindex + remainIndex))
            break
    print(indexlist)

    with Pool(processes=np) as pl:
        pl.map(multiprocessSample, indexlist)


# return rs


if __name__ == "__main__":
    # userlist = list()
    # for i in range(10000):
    #     userlist.append(i)
    #  print(i)
    start = time.time()
    startprocessing()
    end1 = time.time() - start
    print(end1)
    sum = 0
    start = time.time()
    insertSample(0, len(userlist))
    end2 = time.time() - start

    print(end2)
    # print(sum)

