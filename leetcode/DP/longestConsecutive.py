# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: longestConsecutive.py
@time:2020-03-02 16:23
@file_desc: 
"""
import logging as log
import sys

log.basicConfig(level=log.DEBUG)
_logger = log.getLogger(__name__)


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 遍历寻找所有的链
        # 先更新每个点的连接数

        num_tags = {}
        for num in nums:
            num_tags[num] = 1
        num_links = {}
        num_types = {}
        for num in nums:
            left_tag = int(num_tags.__contains__(num - 1))
            right_tag = int(num_tags.__contains__(num + 1))
            num_links[num] = left_tag + right_tag
            if left_tag + right_tag == 0:
                num_links[num] = 1
        for k in num_links.keys():
            if num_links[k] == 1:
                num_types[k] = 0
        best = []
        searched = {}
        for k in num_types.keys():
            # 查找序列
            # print("----")
            if searched.__contains__(k):
                pass
            searched[k] = 1
            brk = True
            temp = []
            temp.append(k)
            max_len = 2
            direc = 1
            if num_tags.__contains__(k - direc):
                direc = -1
            searched[k + direc] = 1
            prev = k + direc
            # temp.append(prev)
            # print(prev)

            while num_links.__contains__(prev):
                if num_links[prev] == 2:
                    max_len += 1
                    temp.append(prev)
                    prev += direc
                else:
                    temp.append(prev)
                    break

            if max_len > len(best):
                best = temp

        return best










if __name__ == '__main__':
    solu = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums = [0]
    ans = solu.longestConsecutive(nums)
    a = 20.1
    a = a >> 1
    print(a)

