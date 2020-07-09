# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: notDesc.py
@time:2020-04-29 13:50
@file_desc: 
"""
import logging as log
import sys

log.basicConfig(level=log.DEBUG)
_logger = log.getLogger(__name__)


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            return False
        if l == 1:
            return True
        count = 0
        for i in range(l - 1):
            if count > 1:
                return False
            if nums[i] > nums[i + 1]:
                # 判断能否该nums[i]
                if i == 0 or i == l -2:
                    count += 1
                elif nums[i - 1] <= nums[i + 1]:
                    count += 1
                elif nums[i]<nums[i+2]:
                    count += 1
                else:
                    return False

        if count <= 1:
            return True
        return False

if __name__ == '__main__':
    solu = Solution
    nums = [3,4,2,3]
    ans = solu.checkPossibility(solu, nums)
    print(ans)