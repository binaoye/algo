# Definition for a binary tree node.
from leetcode.tree import printtree
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 使用队列，让右侧元素先进队，对于每个节点输出时，由于队列先进先出，下回就会先输出右侧元素
        # 这种方式相当于从右往左的广度遍历。然鹅这个题要求深度遍历。。。

        queue = deque([])
        queue.appendleft(root)
        last = None
        while queue:
            last = queue.pop()
            print(last.val)
            if last.right:
                queue.appendleft(last.right)
            if last.left:
                queue.appendleft(last.left)
        return last.val




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

    ans = solu.findBottomLeftValue(solu, root)
    print('ans', ans)




