import leetcode.Linklist.PrintLinkList
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printLinklist(self, root):
        ret = []
        while root:
            ret.append(root.val)
            root = root.next
        print(ret)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 使用归并排序，每次去除最小
        stack = []
        for lst in lists:
            while lst:
                stack.append(lst)
                lst = lst.next
        ans,aus = self.merge(self,stack)
        return ans


    def merge(self, stack):
        if stack:
            # 取出栈顶节点
            node = stack.pop()
            min = node.val
            start = node
            end = node
            left = []
            right = []
            while stack:
                nd = stack.pop()
                if nd.val < min:
                    left.append(nd)
                else:
                    right.append(nd)
            left_start, left_end = self.merge(self,left)
            right_start, right_end = self.merge(self,right)
            if left_start is None and right_start is None:
                node.next = None
                return start, end
            if left_start and right_start:
                left_end.next = node
                node.next = right_start
                return left_start, right_end
            if left_start and right_start is None:
                left_end.next = node
                return left_start, node
            if left_start is None and right_start:
                node.next = right_start
                return node, right_end
        else:
            return None, None






if __name__ == "__main__":
    root1 = ListNode(1)
    rootnode2 = ListNode(2)
    rootnode3 = ListNode(4)
    root1.next = rootnode2
    rootnode2.next = rootnode3
    root1.printLinklist(root1)
    root2 = ListNode(1)
    rootnode4 = ListNode(3)
    rootnode5 = ListNode(4)
    rootnode6 = ListNode(7)
    root2.next = rootnode4
    rootnode4.next = rootnode5
    rootnode5.next = rootnode6
    root2.printLinklist(root2)


    solu = Solution
    lst = []
    lst.append(root1)
    lst.append(root2)
    ans = solu.mergeKLists(solu, lst)

    ans.printLinklist(ans)

    x = []
    if x:
        print("sdfa")
    else:
        print("fjhfg")