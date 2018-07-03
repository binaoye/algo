class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        num1 = self.calc(self, height)
        # height.reverse()
        # num2 = self.calc(self, height)
        return num1 + 0

    def calc(self, height):
        left, right = 0, 0
        rain = []
        ans = 0
        for n in height:
            if n < left:
                rain.append(n)
            else:
                # 开始一个新的边界
                if len(rain) > 0:
                    # 结算雨量
                    right = n
                    print('得到一个坑', left, right, rain, (len(rain) * min(left, right) - sum(rain)))
                    ans += (len(rain) * min(left, right) - sum(rain))
                left = n
                rain = []
        return ans



if __name__ == "__main__":
    solu = Solution
    ans = solu.trap(solu, [0,1,0,2,1,0,1,3,2,1,2,1,2])
    print(ans)