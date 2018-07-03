import sys
import time
import copy
def cmp(x, y):
    if x >= y:
        return x
    else:
        return y
def timebigger(left, right):
    lspl = left.split(":")
    rspl = right.split(":")
    lmins = int(lspl[0]) * 60 + int(lspl[1])
    rmins = int(rspl[0]) * 60 + int(rspl[1])
    return lmins > rmins
if __name__ == "__main__":
    s = [1,2,3]
    print(s)
    s.append([10])
    print(s)
    x = {}
    x[1] = 2
    x[2] = 2
    x[3] = 2
    # y = {i:0 for i in range(10)}
    # y[1] += 10
    # print(y)
    y = sorted(x.items(), key=lambda d:d[1],reverse=True)
    for k,v in y:
        print(k,v)
    # weights = list(map(int, sys.stdin.readline().strip().split()))
    # print(weights)
    if ~(1 > 2):
        print("sdfs")

    start = time.time()
    lst = [1]
    for i in range(10000):
        lst.append("12:00">"13:00")

    stop1 = time.time()

    for j in range(10000):
        lst.append(timebigger("12:00", "13:00"))
    stop2 = time.time()

    print("first", stop1 - start)
    print("second", stop2 - start)

    lst = [[1],[2],[3]]
    x = copy.copy(lst.__getitem__(1))
    print(x)
    x.append(6)
    print(lst)
    print("00:30">"12:00")
    y = x[:]