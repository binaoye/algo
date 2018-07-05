class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("-------")
        print(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])
        mid = int((len(nums))/2)
        print('mid',nums[mid])
        print('left', nums[0:mid])
        print('right', nums[mid:])
        leftans = self.maxSubArray(self,nums[0:mid])
        rightans = self.maxSubArray(self, nums[mid:])
        print('leftans', leftans)
        print('rightans', rightans)
        leftboard = 0
        rightboard = 0
        leftmax = nums[mid-1]
        rightmax = nums[mid]
        for i in range(mid):
            leftboard += nums[mid - 1 - i]
            if leftboard > leftmax:
                leftmax = leftboard
        for j in range(mid, len(nums)):
            rightboard += nums[j]
            if rightboard > rightmax:
                rightmax = rightboard
        print('leftmax', leftmax)
        print('ans', max(leftmax+rightmax, leftans, rightans))
        return max(leftmax+rightmax, leftans, rightans)








if __name__ == "__main__":
    solu = Solution
    x = solu.maxSubArray(solu, nums = [2,0,3,-2])
    # x = solu.maxSubArray(solu, nums=[1,-1,1])
    print('ans', x)
    for i in range(0):
        print("*****")
