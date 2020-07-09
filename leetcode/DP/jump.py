# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: jump.py
@time:2020-04-27 14:35
@file_desc: 
"""

import time

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        jp, pos, res = 0, 0, 0
        # while res < l - 1:
            

        return jp




if __name__ == '__main__':
    st = time.time()
    solu = Solution
    nums = [1,1,1,1]
    print(solu.jump(solu, nums))

    # nums.append(100)

    nums = [1]
    for i in range(10000):
        nums = [0] + nums
        a = min(nums[0:3])
    ends = time.time()

    print(ends-st)






