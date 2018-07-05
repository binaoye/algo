class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums.pop()
        count = 1
        while nums:
            num = nums.pop()
            if num == maj:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maj = num
                    count = 1
        return num
