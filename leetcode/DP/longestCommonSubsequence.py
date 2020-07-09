# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: longestCommonSubsequence.py
@time:2020-04-09 15:00
@file_desc: 
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]  # dp[i][j] 代表text1[0:i], text2[0:j]的公共子序列
        ans = 0
        # print(dp)

        # 定义状态转移方程
        # 当text1[i]==text2[j]时dp[i][j]=dp[i-1][j-1]+1
        # 否则dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        for i in range(1, len(text1)+1):
            # for l in dp:
            #     print(l)
            # print('-----')
            for j in range(1, len(text2)+1):
            #     # print(i, j)
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    # print(text1[i - 1], i, j, dp[i][j], ans)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                ans = max(dp[i][j], ans)
        # print(dp)
        for l in dp:
            print(l)
        return ans





if __name__ == '__main__':
    # text1 = "bsbininm"
    # text2 = "jmjkbkjkv"
    # text1, text2 = "abcde", "abc"
    # text1, text2 = "oxcpqrsvwf", "shmtulqrypy"
    text1, text2 = "pmjghexybyrgzczy", "hafcdqbgncrcbihkd"
    solu = Solution
    print(solu.longestCommonSubsequence(solu, text1, text2))
    # sp = [[0] * 3]*4
    # print(sp[3][2])