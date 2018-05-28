import sys
if __name__ == "__main__":
    # # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)

    # 读取数据
    n,m = map(int, sys.stdin.readline().strip().split())
    # 满减价格
    total_price = 0
    # 特价价格
    total_onsale = 0
    max_thres = 0

    for i in range(n):
        s,t = map(int, sys.stdin.readline().strip().split())
        total_price += s
        if t == 1:
            total_onsale += s * 0.8
    min_price = total_price
    for j in range(m):
        thres, disc = map(int, sys.stdin.readline().strip().split())
        if total_price >= thres:
            price_discount = total_price - disc
            min_price = min(min_price, price_discount)

    print('%.2f' % min(min_price, total_onsale))