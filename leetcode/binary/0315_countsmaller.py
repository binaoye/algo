class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class Solution(object):
    def countSmaller(self, nums):
        sortedList = []
        output = [0] * len(nums)
        for i in range(len(nums)):
            left, right = 0, len(sortedList) - 1
            index = len(nums) - 1 - i
            while left <= right:
                mid = left + (right - left) // 2
                if sortedList[mid] < nums[index]:
                    left = mid + 1
                else:
                    right = mid - 1
            sortedList.insert(left, nums[index])
            output[index] = left
            print('output', output)
            print('sortedlist', sortedList)
        return output

        # hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        # print('nums', nums)
        # print('hasthtable', hashTable)
        # tree, r = BinaryIndexedTree(len(hashTable)), []
        # for i in range(len(nums) - 1, -1, -1):
        #     # 从右往左,依次遍历
        #     r.append(tree.sum(hashTable[nums[i]]))
        #     tree.update(hashTable[nums[i]] + 1)
        #     print('r', r)
        #     print('tree', tree.sums)
        # return r[::-1]




if __name__ == "__main__":
    solu = Solution
    print(solu.countSmaller(solu, [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))
    i = 12
    i -= i & -i
    print(i)
    print(bin(12))
    print(bin(-12))