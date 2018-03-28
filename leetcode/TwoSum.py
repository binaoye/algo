class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            n = nums[i]
            for x in range(i + 1,len(nums)):
                if nums[i] + nums[x] == target:
                    return [i,x]




if __name__ == "__main__":
    solu = Solution
    print(solu.twoSum(solu,[0,0],0))