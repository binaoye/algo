# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: checkSubarraySum.py
@time:2020-04-29 17:13
@file_desc: 
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        if l<=1:
            return False
        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        for i in range(1, l):
            dp[i] = dp[i-1] + nums[i]

        for i in range(l):
            for j in range(i+1, l):
                su = dp[j] - dp[i] + nums[i]
                if su ==0 or su%k == 0:
                    return True
        return False


if __name__ == '__main__':
    solu = Solution
    nums = [1, 2, 12]
    k = 6
    print(solu.checkSubarraySum(solu, nums, k))
    # print(1%2)