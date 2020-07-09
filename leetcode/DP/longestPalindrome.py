# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: longestPalindrome.py
@time:2020-02-20 19:42
@file_desc: 
"""
import logging as log
import sys


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        # 中心扩展法
        def expand(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        end = 0
        max_len = 0
        for i in range(len(s) - 1):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            lens = max(len1, len2)
            if lens > max_len:
                max_len = lens
                start = i - (lens - 1) // 2
                end = i + lens // 2
        print(int(start), int(end))
        return s[start:end + 1]

if __name__ == '__main__':
    solu = Solution
    print(solu.longestPalindrome(solu, str('cbbcddddddd')))