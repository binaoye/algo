import sys

def findpath(paths, k, maxtime=1e9):
    ans_driver = []
    ans_dest = []
    alldist = []
    for k, v in paths.items():
        for s,x in v.items():
            alldist.append(x)
    if min(alldist) > maxtime:
        return ans_driver, ans_dest, paths







if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    # e = [['N' for i in range(n + 1)] for j in range(n + 1)]
    # for i in range(m):
    #     line = list(map(int, sys.stdin.readline().strip().split()))
    #     e[line[0]][line[1]] = line[2]
    #
    # for i in range(1,n):
    #     e[i][0] = min(e[i][1:])
    #     e[0][i] = min(e[1:][i])
    # for x in e:
    #     print(x)
    #
    # print(e[1][1:])
    e = []
    for i in range(m):
        e.append(list(map(int, sys.stdin.readline().strip().split())))
    print(e)
    # 外卖小哥编号作为key，value为其所有的路线列表，路线存储方式为以目的地为key，时间为value的字典
    dic = {}
    for lst in e:
        driver = str(lst[0])
        pth = {}
        dest = str(lst[1])
        dist = lst[2]
        if driver not in dic.keys():
            pth[dest] = lst[2]
        else:
            pth = dic[driver]
            if dest not in pth.keys():
                pth[dest] = lst[2]
            else:
                pth[dest] = min(pth[dest], lst[2])
        dic[driver] = pth
    print(dic)
    # dic.__delitem__('1')
    # print(dic)
    _,_,_ = findpath(dic, 10, 6)

