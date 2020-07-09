# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: num_decoding.py
@time:2020-02-20 20:11
@file_desc: 
"""
import logging as log
import sys


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 1
        # ans = [[0] * len(s)] * len(s)  # s[i:j]的编码种数
        # a[0][0] = 1

        ans = [1] * (len(s) + 1)
        ans[0] = 0
        for i in range(2, len(s) + 1):
            if int(s[i - 1:i]) > 26:
                ans[i] = ans[i - 2] + 1

        return ans[len(s)]

if __name__ == '__main__':
    # solu = Solution
    # print(solu.numDecodings(solu, '226'))
    s = '012'
    a = [[0] * len(s)] * len(s)
    print(a[0][1])
    print(s[0:2])
