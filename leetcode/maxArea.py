# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: maxArea.py
@time:2020-04-27 13:32
@file_desc: 
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,res = 0, len(height) -1, 0
        while(i < j):
            res = max(res, (min(height[i], height[j])) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    solu = Solution
    nums = [1,8,6,2,5,4,8,3,7]
    print(solu.maxArea(solu, nums))