# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: lengthOfLIS.py
@time:2020-04-09 14:44
@file_desc: 
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<=1:
            return l
        dp = [1] * l # 截止当前的最长上升序列
        for i in range(1, l):
            prev = []
            for j in range(i):
                if nums[j]<nums[i]:
                    prev.append(dp[j])
            if len(prev)>0:
                dp[i] = max(prev) + 1

        # print(dp)
        return max(dp)






if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    solu = Solution
    solu.lengthOfLIS(solu, nums)
