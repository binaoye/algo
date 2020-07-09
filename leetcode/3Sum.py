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

    def tSum(self, nums):
        if len(nums) < 3:
            return []
        # 排序
        nums = sorted(nums)
        if nums[0]>0 or nums[-1]< 0:
            return []
        if nums[0] == 0 and nums[-1] == 0:
            return [[0, 0, 0]]
        lens = len(nums)
        res = []
        # print(nums)
        for i in range(lens):
            # print(nums[i], nums[i-1])
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print('no pass')
            l = i + 1
            r = lens - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    # print("res", nums[i], nums[l], nums[r])
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                    # c.add(str(nums[i]) + ',' + str(nums[l]) + ',' + str(nums[r]))
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        # ans = [[int(z) for z in x.split(',')] for x in list(c)]
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
    # s = [-1,0,1,0]
    s = [-1,0,1,2,-1,-4]
    # s = [0, 0, 0, 0, 0, 0]
    solu = Solution
    # s.sort()
    # print(solu.twoSum(solu,[0,0],0))
    # print(solu.threeSum(solu,s))
    print(solu.tSum(solu, s))
