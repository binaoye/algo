from leetcode.tree import printtree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.val is None:
            return []
        leftans = self.largestValues(self, root.left)
        rightans = self.largestValues(self, root.right)
        ans = []
        ans.append(root.val)
        if root.left is None:
            print(root.val,'\t', leftans,'\t', rightans, '\t', ans)
            return ans + rightans
        elif root.left.val is None:
            return ans + rightans
        if root.right is None:
            print(root.val, '\t', leftans, '\t', rightans, '\t', ans)
            return ans + leftans
        elif root.right.val is None:
            return ans + leftans
        leftans.reverse()
        rightans.reverse()
        while leftans or rightans:
            if not leftans:
                print(root.val, '\t', leftans, '\t', rightans, '\t', ans)
                rightans.reverse()
                return ans + rightans
            if not rightans:
                print(root.val, '\t', leftans, '\t', rightans, '\t', ans + leftans, 'tag1')
                leftans.reverse()
                return ans + leftans
            l = leftans.pop()
            r = rightans.pop()
            ans.append(max(l, r))
        print(root.val, '\t', leftans, '\t', rightans, '\t', ans)
        return ans



if __name__ == "__main__":
    # root = TreeNode(5)
    # n1 = TreeNode(4)
    # n2 = TreeNode(11)
    # root.left = n1
    # n1.right = n2
    # # root.right = n2
    # n3 = TreeNode(8)
    # n4 = TreeNode(13)
    # n5 = TreeNode(2)
    # n1.left = n3
    # n3.left = n4
    # n3.right = n5
    # n6 = TreeNode(3)
    # n6.right = TreeNode(9)
    # n7 = TreeNode(4)
    # n7.left = TreeNode(15)
    # n2.left = n6
    # n2.right = n7
    # n7.right = TreeNode(1)
    root = TreeNode(98)
    n1 = TreeNode(97)
    n2 = TreeNode(88)
    n3 = TreeNode(84)
    n4 = TreeNode(79)
    n5 = TreeNode(87)
    n6 = TreeNode(64)
    n7 = TreeNode(63)
    n8 = TreeNode(69)
    n9 = TreeNode(62)
    root.left = n1
    n1.left = n2

    n2.left = n3
    n3.left = n4
    n3.right = n5
    n4.left = n6
    n6.left = n7
    n7.left = n9
    n6.right = n8
    printtree.Pretty_print(n3)
    solu = Solution
    ans = solu.largestValues(solu, root)
    print(ans)