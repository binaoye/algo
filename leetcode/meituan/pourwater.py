import sys

def calcAdjust(temp, capicity, target, intemp):
    ans = 0
    for i in range(len(temp)):
        ans += adjust(temp[i], capicity[i], target, intemp)
    return ans, target


def adjust(t, c, target, intem):
    if target == intem:
        return 0
    return c * (t - target) / (target - intem)

def mixAll(temp, capicity, T, C):
    su = 0
    cc = 0
    for i in range(len(temp)):
        cc += capicity[i]
        su += temp[i] * capicity[i]
    su += T * C
    cc += C
    return su / cc



if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    tot_temp, tot_cap = map(int, sys.stdin.readline().strip().split())
    capicity = []
    temp = []
    for i in range(n):
        tmp, cap = map(int, sys.stdin.readline().strip().split())
        temp.append(tmp)
        capicity.append(cap)
    temp_min = min(temp)
    temp_max = max(temp)
    water = []
    target = 0
    flag = False
    if tot_temp < temp_min:
        flag = True
        water, target = calcAdjust(temp, capicity, temp_min, tot_temp)
    elif tot_temp > temp_max:
        flag = True
        water, target = calcAdjust(temp, capicity, temp_max, tot_temp)
    if temp_max == temp_min:
        flag = True
        water = 0
        target = temp_min
    if flag and water <= tot_cap:
        if tot_temp > target:
            target = mixAll(temp, capicity, tot_temp, tot_cap)
        print("Possible")
        print('%.4f' % target)
    else:
        print("Impossible")

