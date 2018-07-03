import sys
import time
import copy
class train:
    def __init__(self, x, y, price, xtime, ytime):
        self.x = x
        self.y = y
        self.price = price
        self.xtime = xtime
        self.ytime = ytime

class city:
    def __init__(self, num):
        self.num = num
        # train 与 next对应的城市顺序一致
        self.next = []
        self.trains = []
    # 添加当前城市出发的路线
    def addTrain(self, c):

        self.trains.append(c)
        if c.y not in self.next:
            # print(self.num , ' add next', c.y.num)
            self.next.append(c.y)

    # 获取到某城市的车次
    def getCityTrain(self, c, time):
        result = []
        if c in self.next:
            for i in self.trains:
                if i.y == c:
                    if timebigger(i.xtime, time):
                        result.append(i)
                    elif self.num == 1:
                        if time == "00:00":
                            result.append(i)

        return result
    def __str__(self):
        return 'City No:', self.num

class path:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        # 下一条节点列表，[[city]]
        self.citylist = []
        # 下一条使用路线， [[train]]
        self.trainlist = []

# 路线图
class cityGraph:
    def __init__(self):
        # print("----")
        self.citys = []
        self.cityids = []
        self.d = {}
        self.ids = {}
        self.addCity(1)
    # 添加城市到图中
    def addCity(self, num):
        startCity = city(num)
        self.citys.append(startCity)
        self.cityids.append(startCity.num)
        self.ids[str(num)] = startCity
        return startCity

    # 根据id从图中查找城市
    def getCity(self, num):
        if num not in self.cityids:
            ct = self.addCity(num)
            return ct
        else:
            return self.ids[str(num)]

    # 按行读入图
    def cityFromLine(self, line):
        spl = line.split(" ")
        # print(line)
        # 处理城市
        startCity = self.getCity(int(spl[0]))
        endCity = self.getCity(int(spl[1]))
        # 处理路线
        newtrain = train(startCity, endCity, int(spl[2]), spl[3], spl[4])
        startCity.addTrain(newtrain)

    # 查找路线，广度遍历
    def searchPath(self, start, end, time):
        result = path(start, end)
        key = "_".join([str(start.num), str(end.num), time])
        # key = str(start.num) + '_' + str(end.num) + '_' + time
        if key in self.d.keys():
            answer = self.d[key]
            return answer
        # print('当前起点：', start.num, ' 终点：', end.num)
        # 递归出口，返回路线列表与节点顺序列表，数据结构为以起点为key的map
        if len(start.next) == 0:
            return result
        ncity = []
        ntrain = []
        if end in start.next:
            xtrain = start.getCityTrain(end, time)
            # print(start.num, '直达', end.num, xtrain.__len__())
            for x in xtrain:
                ncity.append([end])
                ntrain.append([x])
        # 回溯
        for ct in start.next:
            if ct != end:
                xtrain = start.getCityTrain(ct, time)
                # 下一跳的列车选择时，必须保证如果错过还有别的路线选择
                # 合并结果集，不包含当前节点，只包含之后的节点
                for z in xtrain:
                    nkey = str(ct.num) + '_' + str(end.num) + '_' + z.ytime
                    if nkey in self.d.keys():
                        answer = self.d[nkey]
                    else:
                        answer = self.searchPath(ct, end, z.ytime)
                    if answer.citylist.__len__() >= 1:
                        # print('起点:', ct.num, '终点', end.num, '找到路径', answer.citylist)
                        for i in range(answer.citylist.__len__()):
                            # print('附加', start.num, '到', ct.num, '时间', z.xtime)
                            shx = copy.copy(answer.citylist[i])
                            shx.insert(0, ct)
                            shy = copy.copy(answer.trainlist[i])
                            shy.insert(0, z)
                            ncity.append(shx)
                            ntrain.append(shy)
        result.trainlist = ntrain
        result.citylist = ncity
        # 结果先存起来

        self.d[key] = result
        return result
    def timeAdd(self, time):
        tspl = time.split(':')
        h = 0
        m = 0
        if int(tspl[1]) == 30:
            h = int(tspl[0]) + 1
            m = 0
        else:
            h = int(tspl[0])
            m = 30
        return str(h) + ':' + str(m)


    def choosePath(self, primaryResult, start, end):
        # 先选择删除最晚出发的一条路线
        # print('剪枝前路线数量', primaryResult.trainlist.__len__())
        starttime = "00:00"
        ntrain = primaryResult.trainlist
        ncity = primaryResult.citylist
        result = path(start, end)
        for i in range(len(ntrain)):
            # print('比较时间', ntrain[i][0].xtime, ncity[i][0].num)
            if timebigger(ntrain[i][0].xtime, starttime):
                starttime = ntrain[i][0].xtime
            elif ntrain[i][0].xtime == starttime:
                starttime = ntrain[i][0].xtime
        # print('删除的出发时间为', starttime)
        # 删除最晚的路线
        cityresult = []
        trainresult = []
        while ntrain:
            tr = ntrain.pop()
            ct = ncity.pop()
            if tr[0].xtime != starttime:
                cityresult.append(ct)
                trainresult.append(tr)
        # print('删除后的路线数', cityresult.__len__())
        result.trainlist = trainresult
        result.citylist  = cityresult
        dtrain = []
        dcity = []
        # 遍历所有的结果集
        l = len(result.trainlist)
        for i in range(l):
            # 对于每一趟车，判断如果没赶上有更多车可以补救
            flag = True
            # print("*****************")
            for t in result.trainlist[i]:
                # print('---------------')
                if self.checkPath(t.x, end, t.xtime):
                    # print(t.x.num, t.y.num, t.xtime, '无法换乘')
                    flag = False
            if flag:
                dtrain.append(result.trainlist[i])
                dcity.append(result.citylist[i])
        result.trainlist = dtrain
        result.citylist = dcity
        # print('剪枝后路线数量', dtrain.__len__())
        return result

    def checkPath(self, start, end, time):
        key = str(start.num) + '_' + str(end.num) + '_' + time
        # print("check ", key)
        if key in self.d.keys():
            answer = self.d[key]
        else:
            answer = self.searchPath(start, end, time)
        for t in answer.trainlist:
            # print('比较', t[0].xtime, time, timebigger(t[0].xtime, time))
            if timebigger(t[0].xtime, time):
                return False
        return True

    def findCheapest(self, r):
        min_price = []
        l = len(r.citylist)
        for i in range(l):
            for t in r.trainlist:
                tot = 0
                for ft in t:
                    tot += ft.price
                min_price.append(tot)
        return min(min_price)

def timebigger(left, right):
    lspl = left.split(":")
    rspl = right.split(":")
    lmins = int(lspl[0]) * 60 + int(lspl[1])
    rmins = int(rspl[0]) * 60 + int(rspl[1])
    return lmins > rmins


if __name__ == "__main__":
    # 读取数据
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = cityGraph()
    lines = []
    # print('m', m)
    for i in range(m):
        lines.append(sys.stdin.readline().strip())
    for line in lines:
        graph.cityFromLine(line)
    start = time.time()
    city1 = graph.getCity(1)
    city3 = graph.getCity(n)
    answer = graph.searchPath(city1, city3, "00:00")
    result = graph.choosePath(answer, city1, city3)

    if len(result.citylist) >= 1:
        print(graph.findCheapest(result))
    else:
        print(-1)
    stop = time.time()
