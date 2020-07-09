# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: shortestSubarray.py
@time:2020-04-29 19:26
@file_desc: 
"""

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # A= sorted(A, reverse=True)
        dp = [A[0] for i in range(len(A))]
        for l in A:
            if l>K:
                return 1
        for i in range(1, len(A)):
            dp[i] = dp[i-1] + A[i]
        print(dp)
        for l in range(len(A)):
            for s in range(len(A)-l):
                print(dp[l+s], dp[s])
                su = dp[l+s] - dp[s] + A[s]
                if su>=K:
                    return l+1
        return -1

if __name__ == '__main__':
    A = [1]
    K = 1
    solu = Solution
    print(solu.shortestSubarray(solu, A, K))
