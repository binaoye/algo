class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mid, left, right, left_num, right_num = self.partition(self, nums)
        print("---")
        while right_num != k - 1:
            print("---")
            print(k)
            if right_num > k - 1:
                # 从右侧找
                print("right")
                mid, left, right, left_num, right_num = self.partition(self, right)
            else:
                # 从左侧找
                print("left")
                k = k - right_num - 1
                mid, left, right, left_num, right_num = self.partition(self, left)

        return mid

    def partition(self, all):
        print(all)
        mid = all.pop()
        left_num = 0
        right_num = 0
        left = []
        right = []
        while all:
            x = all.pop()
            if x > mid:
                right.append(x)
                right_num += 1
            else:
                left.append(x)
                left_num += 1
        return mid, left, right, left_num, right_num




if __name__ == "__main__":
    nums = [-1, -1]
    solu = Solution
    ans = solu.findKthLargest(solu, nums, 2)
    print(ans)