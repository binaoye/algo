# Definition for a binary tree node.
from leetcode.tree import printtree
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = deque([])
        temp = deque([])
        stack.appendleft(root)
        count = 1
        while stack:
            count -= 1
            node = stack.pop()
            if node.left:
                temp.appendleft(node.left)
            if node.right:
                temp.appendleft(node.right)
            if count == 0:
                stack = temp
                count = stack.__len__()
                ans.append(node.val)
        return ans



if __name__ == "__main__":
    solu = Solution
    root = TreeNode(5)
    n1 = TreeNode(4)
    n2 = TreeNode(8)
    root.left = n1
    root.right = n2
    n3 = TreeNode(11)
    n4 = TreeNode(7)
    n5 = TreeNode(2)
    n1.left = n3
    n3.left = n4
    n3.right = n5
    n6 = TreeNode(13)
    n6.right = TreeNode(9)
    n7 = TreeNode(4)
    n7.left = TreeNode(15)
    n2.left = n6
    n2.right = n7
    # n7.right = TreeNode(1)
    printtree.Pretty_print(root)

    ans = solu.rightSideView(solu, root)
    print(ans)