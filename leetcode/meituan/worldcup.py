import sys

if __name__ == "__main__":
    rate = []
    for i in range(16):
        nums = map(float, sys.stdin.readline().strip().split())
        rate.append(nums)
    finaleight = []
    finalfour = []
    finaltwo = []
    # 先计算八分之一决赛
    for i in range(8):
        finaleight[2 * i] = rate[2 * i][2 * i + 1]
        finaleight[2 * i + 1] = rate[2 * i + 1][2 * i]

    # 再计算四强：
    # for j in range(4):
