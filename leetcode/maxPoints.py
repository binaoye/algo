# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: maxPoints.py
@time:2020-04-29 15:17
@file_desc: 
"""



class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        le = len(points)
        if le <= 2:
            return le
        dp = [['sb' for i in range(le)] for j in range(le)]
        ans = 1
        for i in range(le):
            for j in range(i+1, le):
                print('---')
                k = 'max'
                if points[i][0] != points[j][0]:
                    k = str(1.0 * (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]))
                elif points[i][1] == points[j][1]:
                    k = 'sb'
                dp[i][j] = k
                dp[j][i] = k
            # 计算该点跟多少个点共线
            tmp = {'t':0}
            same = 0
            for x in range(le):
                print('++++++')
                print(dp[i])

                if dp[i][x] == 'sb':
                    same += 1
                elif dp[i][x] in tmp.keys():
                    tmp[dp[i][x]] += 1
                else:
                    tmp[dp[i][x]] = 1
                # print(tmp, ans)
            print(tmp)
            ans = max(ans, max(tmp.values())+same)
            print(same, max(tmp.values()), ans)
        for l in dp:
            print(l)
        return ans

if __name__ == '__main__':
    solu = Solution
    points = [[0,0],[94911151,94911150],[94911152,94911151]]
    solu.maxPoints(solu, points)

