import sys
def cmp(x, y):
    if x >= y:
        return x
    else:
        return y

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