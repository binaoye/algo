class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)
        while left < right:
            small, large = 0, 0
            mid = int((left + right)/2)
            for n in nums:
                if n >= left and n <= mid:
                    small += 1
                elif n <= right and n > mid:
                    large += 1
            if left + small > mid + 1:
                right = mid
            else:
                left = mid + 1
        return left







if __name__ == "__main__":
    solu = Solution
    ans = solu.findDuplicate(solu, [1,3,4,2,2])
    print(ans)