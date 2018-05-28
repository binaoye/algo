import sys

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().strip().split())
    all = []
    a, b = map(int, sys.stdin.readline().strip().split())
    all.append(0)
    maxinde = 0
    maxnum = a * m / n + b * (n - m) / n
    for i in range(k - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        expect = a * m / n + b * (n - m) / n
        if expect >= maxnum:
            maxnum = expect
            maxinde = i
        all.append(0)
    all[maxinde] = n
    print(str(all).replace("[","").replace("]","").replace(",",""))