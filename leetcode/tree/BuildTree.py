from leetcode.tree import printtree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    # 递归版本
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        print("--------")
        print("in:",inorder)
        print("po:",postorder)
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if postorder:
            mid = postorder.pop()
            midindex = 0
            for x in range(len(inorder)):
                if mid == inorder[x]:
                    midindex = x
                    break
            leftans = self.buildTree(self, inorder[0:midindex], postorder[0:midindex])
            rightans = self.buildTree(self, inorder[midindex+1:], postorder[midindex:])
            root = TreeNode(mid)
            if leftans:
                root.left = leftans
            if rightans:
                root.right = rightans
            return root
        else:
            return None





if __name__ == "__main__":
    solu = Solution
    root = TreeNode(3)
    root.left = TreeNode(9)
    right = TreeNode(20)
    right.left = TreeNode(15)
    right.right = TreeNode(7)
    root.right = right
    print("答案")
    printtree.Pretty_print(root)
    # inorder = [9,3,15,20,7]
    # postorder = [9,15,7,20,3]
    inorder = [1,2,3,4]
    postorder = [4,3,2,1]
    # print(inorder.i)
    ans = solu.buildTree(solu, inorder, postorder)
    print("结果")
    printtree.Pretty_print(ans)