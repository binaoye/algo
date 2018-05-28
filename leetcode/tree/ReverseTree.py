from leetcode.tree import printtree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def reverseTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """





if __name__ == "__main__":
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
    n7.right = TreeNode(1)
    printtree.Pretty_print(root)

    solu = Solution