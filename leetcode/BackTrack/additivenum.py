class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # 确定起始位置
        # if len(num) < 3:
        #     return False
        # l = int((len(num) - 1)/2) + 1
        # for i in range(1, l):
        #     if num[0] == '0' and i > 1:
        #         break
        #
        #     for j in range(i + 1, i + l):
        #         if num[i] == '0' and j - i > 1:
        #             break
        #         flag, pos, num1, num2 = self.search(self, int(num[0:i]), int(num[i:j]), num, j)
        #         while flag:
        #             if pos == len(num):
        #                 return True
        #             flag, pos, num1, num2 = self.search(self, num1, num2, num, pos)
        # return False
        n = len(num)
        for i, j in self.firstTwo(self, n, num[0] == "0"):
            if num[i] == "0" and j - i > 1: continue
            a, b, cur = num[:i], num[i:j], j
            while True:
                c = str(int(a) + int(b))
                if num.startswith(c, cur):
                    cur += len(c)
                    if cur == n: return True
                    a, b = b, c
                else:
                    break
        return False


    def search(self, num1, num2, num, start):
        if num[start] == '0':
            if num1 + num2 > 0:
                return False, 1, 0, 0
            else:
                return True, start + 1, 0, 0
        sumnum = num1 + num2
        l = len(str(sumnum))
        if l > (len(num) - start):
            return False, 0, 0, 0
        if sumnum - int(num[start:start+l]) == 0 and num[start] != '0':
            # print(start + l, num2, num1)
            return True, start + l, num2, num1 + num2
        return False, 1, 0, 0

    def firstTwo(self, n, zero):
        limit = 2 if zero else (n - 1) / 2 + 1
        for i in range(1, limit):
            j = i + 1
            while n - j >= max(i, j - i):
                yield (i, j)
                j += 1



if __name__ == "__main__":
    solu = Solution
    ans = solu.isAdditiveNumber(solu, "199001200")
    print(ans)