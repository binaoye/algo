import sys

class train:
    def __init__(self, x, y, price, xtime, ytime):
        self.x = x
        self.y = y
        self.price = price
        self.xtime = xtime
        self.ytime = ytime
    def __str__(self):
        return str(self.x.num) + '到' + str(self.y.num) + '价格为' + str(self.price) + '开点' + self.xtime + '到达' + self.ytime
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
            print(self.num , ' add next', c.y.num)
            self.next.append(c.y)

    # 获取到某城市的车次
    def getCityTrain(self, c, time):
        result = []
        if c in self.next:
            for i in self.trains:
                if i.y == c and timebigger(i.xtime, time):
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
        print("----")
        self.citys = [city(1)]
        self.cityids = [1]
    # 添加城市到图中
    def addCity(self, num):
        startCity = city(num)
        self.citys.append(startCity)
        self.cityids.append(startCity.num)
        return startCity

    # 根据id从图中查找城市
    def getCity(self, num):
        if num not in self.cityids:
            ct = self.addCity(num)
            return ct
        else:
            for x in range(len(self.cityids)):
                if self.cityids[x] == num:
                    return self.citys[x]

    # 按行读入图
    def cityFromLine(self, line):
        spl = line.split(" ")
        print(line)
        # 处理城市
        startCity = self.getCity(int(spl[0]))
        endCity = self.getCity(int(spl[1]))
        # 处理路线
        newtrain = train(startCity, endCity, int(spl[2]), spl[3], spl[4])
        startCity.addTrain(newtrain)
    # 判断是否存在路线, 递归
    def getFromTo(self, start, end, time):
        if len(start.next) == 0:
            return False
        # 递归条件：直达
        if end in start.next:
            for train in start.trains:
                if (train.y == end) and (timebigger(train.xtime, time)):
                    return True
        # 查找下一站路线
        for c in start.next:
            ntrain = start.getCityTrain(c, time)
            if ntrain:
                if self.getFromTo(c, end, ntrain[0].ytime):
                    return True
            return False
        return False
    # 查找路线，广度遍历
    def searchPath(self, start, end, time):
        result = path(start, end)
        print('当前起点：', start.num, ' 终点：', end.num)
        # 递归出口，返回路线列表与节点顺序列表，数据结构为以起点为key的map
        if len(start.next) == 0:
            return result
        ncity = []
        ntrain = []
        if end in start.next:
            print(start.num,'直达',end.num)
            xtrain = start.getCityTrain(end, time)
            if len(xtrain) > 0:
                ncity.append([end])
                ntrain.append([xtrain[0]])

        # 回溯
        for ct in start.next:
            if ct != end:
                xtrain = start.getCityTrain(ct, time)
                answer = self.searchPath(ct, end, xtrain[0].ytime)
                # 合并结果集，不包含当前节点，只包含之后的节点
                if answer.citylist.__len__() >= 1:
                    print('起点:', ct.num, '终点', end.num, '找到路径', answer.citylist)
                    for i in range(answer.citylist.__len__()):
                        x = answer.citylist[i]
                        x.insert(0, ct)
                        y = answer.trainlist[i]
                        y.insert(0, xtrain[0])
                        ncity.append(x)
                        ntrain.append(y)
        result.trainlist = ntrain
        result.citylist = ncity
        return result





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
    print('m', m)
    for i in range(m):
        line = sys.stdin.readline().strip()
        graph.cityFromLine(line)
    city1 = graph.getCity(1)
    city3 = graph.getCity(3)
    ans = graph.getFromTo(city1, city3, "10:00")
    # print(ans)
    # for x in city1.next:
    #     print(x.num)

    answer = graph.searchPath(city1, city3, "00:00")
    for i in answer.citylist:
        print("搜索结果")
        for z in i:
            print(z.num)
    for f in answer.trainlist:
        print("车次情况")
        for x in f:
            print(str(x))
