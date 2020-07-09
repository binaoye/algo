# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: three_step.py
@time:2020-04-08 10:47
@file_desc: 
"""

class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        if n < 3:
            return n
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        return dp[n] % 1000000007

if __name__ == '__main__':
    solu = Solution
    print(solu.waysToStep(solu, 10))

