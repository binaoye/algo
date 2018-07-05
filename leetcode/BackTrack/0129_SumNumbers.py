# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        allnums = [int(i) for i in self.calc(self, root)]
        print(allnums)
        return sum(allnums)



    def calc(self, root):
        if root is None:
            return []
        left_ans = [str(root.val) + i for i in self.calc(self, root.left)]
        right_ans = [str(root.val) + i for i in self.calc(self, root.right)]
        if left_ans == [] and right_ans == []:
            return [str(root.val)]
        return left_ans + right_ans


if __name__ == "__main__":
    root = TreeNode(4)
    node1 = TreeNode(9)
    node2 = TreeNode(0)
    node3 = TreeNode(5)
    node4 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    solu = Solution
    ans = solu.sumNumbers(solu, root)
    print(ans)