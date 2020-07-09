# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: anmoshi.py
@time:2020-04-08 11:15
@file_desc: 
"""

class Solution:
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义dp数组为如果预约第i号，截止目前的最大收益
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return dp[1]
        dp[2] = max(nums[0] + nums[2], nums[1])
        if len(nums) == 3:
            return dp[2]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        print(dp)
        return max(dp[-1], dp[-2])


if __name__ == '__main__':
    solu = Solution
    nums = [1,3,1]
    print(solu.massage(solu, nums))



