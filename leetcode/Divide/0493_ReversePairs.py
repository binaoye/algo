class Solution(object):
    res = 0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.merge_sort(self, nums, 0, len(nums)-1)
        return self.res
    def merge_sort(self, nums, left, right):
        print("--------")
        print("nums", nums)
        print("part", nums[left:right+1])
        if right <= left:
            return
        mid = (left + right) // 2
        # 递归计算左右结果并对左右两次进行排序，加速后序计算垮区域的对数
        self.merge_sort(self, nums, left, mid)
        self.merge_sort(self, nums, mid+1, right)
        # 统计个数
        count = 0
        i, j = left, mid+1
        # 固定左边界，右侧遍历，两侧已排序
        print("********")
        while i <= mid:
            print(i, j)
            if j > right or nums[i] <= 2 * nums[j]:
                i += 1
                self.res += count
            else:
                j += 1
                count += 1
        nums[left:right + 1] = sorted(nums[left:right+1])


if __name__ == "__main__":
    nums = [1,3,2,3,1]
    solu = Solution
    ans = solu.reversePairs(solu, nums)
    print(ans)
