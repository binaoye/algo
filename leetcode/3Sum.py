class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)):
            print("循环中：",nums[i])
            print("计算twosum:",nums[i+1:len(nums)],0-nums[i])
            two = self.twoSum(self,nums[i+1:len(nums)],0-nums[i])
            if len(two) > 1:
                for s in two:
                    lst = [nums[i], s[0], s[1]]
                    if lst not in res:
                        print("添加：",lst)
                        res.append(lst)
        return res

    def twoSum(self,nums, target):
        res = []
        for i in range(len(nums)):
            n = nums[i]
            for x in range(i + 1,len(nums)):
                if nums[i] + nums[x] == target:
                    res.append([nums[i],nums[x]])
        if len(res) > 0:
            print("twosum:",res)
            return res
        return []

    def notexists(self,foo,rst):
        for x in foo:
            if rst == x:
                return False
        return True




if __name__ == "__main__":
    s = [-1,0,1,2,-1,-4]
    solu = Solution
    s.sort()
    print(solu.twoSum(solu,[0,0],0))
    print(solu.threeSum(solu,s))
