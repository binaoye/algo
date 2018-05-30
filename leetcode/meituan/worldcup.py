import sys

if __name__ == "__main__":
    rate = []
    for i in range(16):
        nums = list(map(float, sys.stdin.readline().strip().split()))
        rate.append(nums)
    finaleight = [0 for i in range(16)]
    finalfour = [0 for i in range(16)]
    finaltwo = [0 for i in range(16)]
    champion = [0 for i in range(16)]
    print(rate[1][2])
    finaleight[0] = 1
    # 先计算八分之一决赛
    for i in range(8):
        finaleight[2 * i] = rate[2 * i][2 * i + 1]
        finaleight[2 * i + 1] = rate[2 * i + 1][2 * i]

    # 再计算四强：
    for j in range(4):
        finalfour[4 * j] = finaleight[4 * j] * (rate[4 * j][4 * j + 2]*finaleight[4 * j + 2] + rate[4 * j][4 * j + 3]*finaleight[4 * j + 3])
        finalfour[4 * j + 1] = finaleight[4 * j + 1] * (rate[4 * j + 1][4 * j + 2]*finaleight[4 * j + 2] + rate[4 * j + 1][4 * j + 3]*finaleight[4 * j + 3])
        finalfour[4 * j + 2] = finaleight[4 * j + 2] * (rate[4 *j + 2][4 * j]*finaleight[4 * j] + rate[4 * j + 2][4 * j + 1]*finaleight[4 * j + 1])
        finalfour[4 * j + 3] = finaleight[4 * j + 3] * (rate[4 *j + 3][4 * j]*finaleight[4 * j] + rate[4 * j + 3][4 * j + 1]*finaleight[4 * j + 1])
    # 再计算决赛
    for k in range(2):
        for x in range(4):
            finaltwo[8 * k + x] = 0.0
            for y in range(4):
                finaltwo[8 * k + x] += finalfour[8 * k + x] * finalfour[8 * k + 4 + y] * rate[8 * k + x][8 * k + 4 + y]
        for z in range(4):
            finaltwo[8 * k + 4 + z] = 0.0
            for s in range(4):
                finaltwo[8 * k + 4 + z] += finalfour[8 * k + 4 + z] * finalfour[8 * k + s] * rate[8 * k + 4 + z][8 * k + s]
    # 最后计算夺冠
    for k in range(2):
        for x in range(8):
            champion[8 * k + x] = 0.0
            # 上半区
            if k == 0:
                for y in range(8):
                    m = finaltwo[8 * k + x]
                    n = finaltwo[8 * k + y + 8]
                    p = rate[8 * k + x][8 * k + 8 + y]
                    champion[8 * k + x] += m * n * p
            # 下半区
            if k == 1:
                for z in range(8):
                    m = finaltwo[8 * k + x]
                    n = finaltwo[8 * k + z - 8]
                    p = rate[8 * k + x][8 * k + z - 8]
                    champion[8 * k + x] += m * n * p
            champion[8 * k + x] = round(champion[8 * k + x], 10)
    print(str(champion).replace("[","").replace("]","").replace(",",""))