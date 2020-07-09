from leetcode.tree import printtree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Queue(object):
    def __init__(self):
        self.stacka = []
        self.stackb = []
        self.queue = []

    def inqueue(self, node):
        if node:
            self.queue.append(node.val)
            if self.stacka is None:
                self.stacka.append(node)
            else:
                while self.stacka:
                    x = self.stacka.pop()
                    self.stackb.append(x)
                self.stacka.append(node)
                while self.stackb:
                    y = self.stackb.pop()
                    self.stacka.append(y)

    def outqueue(self):
        if self.stacka:
            x = self.stacka.pop()
            self.queue.pop()
            return x
        else:
            return None


class Solution(object):
    # 递归版本
    def scanRight(self, root):
        ans = Queue()
        if root is None:
            return ans
        if root.left is None and root.right is None:
            ans.inqueue(root)
            return ans
        leftans = self.scanRight(self, root.left)
        rightans = self.scanRight(self, root.right)
        print("---")
        print("当前节点：", root.val)
        print("左：", leftans.queue)
        print("右：", rightans.queue)
        if root.left is None:
            nqueue = Queue()
            nqueue.inqueue(root)
            x = rightans.outqueue()
            while x:
                nqueue.inqueue(x)
                x = rightans.outqueue()
            return nqueue
        if root.right is None:
            nqueue = Queue()
            nqueue.inqueue(root)
            x = leftans.outqueue()
            while x:
                nqueue.inqueue(x)
                x = leftans.outqueue()
            return nqueue
        ans.inqueue(root)
        while rightans.queue:
            x = rightans.outqueue()
            ans.inqueue(x)
            leftans.outqueue()
        while leftans.queue:
            y = leftans.outqueue()
            ans.inqueue(y)

        print("合并：", ans.queue)
        return ans
    # 非递归版本
    def rightSideView(self, root):
        # 广度遍历
        queue = Queue()
        ret = []
        count = 1
        queue.inqueue(root)
        while queue.stacka:
            # 先遍历当前层次，并将下层入队，从左往右入队，最后一个作为输出
            while count > 0:
                node = queue.outqueue()
                count -= 1
                if node.left:
                    queue.inqueue(node.left)
                if node.right:
                    queue.inqueue(node.right)
            ret.append(node.val)
            count = queue.queue.__len__()
        return ret
    #
    #                      5
    #                    /   \
    #                   /     \
    #                  /       \
    #                 /         \
    #                /           \
    #               /             \
    #              /               \
    #             /                 \
    #          4                       8
    #        /   \                   /   \
    #       /     \                 /     \
    #      /       \               /       \
    #     /         \             /         \
    #    11          N           13          4
    #  /   \       /   \       /   \       /   \
    # /     \     /     \     /     \     /     \
    # 7     2     N     N     N     9     15    N




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
    # ans = solu.scanRight(solu, root)
    ans = solu.rightSideView(solu, root)
    print("_______")
    print(ans)