from leetcode.tree import printtree

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        # 快慢指针定位切分点
        node = ListNode(-1)
        node.next = head
        fast = node.next
        slow = node.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            node = node.next
        print('mid', slow.val)
        node.next = None
        righthead = slow.next
        slow.next = None
        left = self.sortedListToBST(self, head)
        right = self.sortedListToBST(self, righthead)
        root = TreeNode(slow.val)
        root.left = left
        root.right = right
        return root




if __name__ == "__main__":
    head = ListNode(-10)
    node1 = ListNode(-3)
    node2 = ListNode(0)
    node3 = ListNode(5)
    node4 = ListNode(9)
    node5 = ListNode(20)
    node6 = ListNode(100)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = node5
    # node5.next = node6
    solu = Solution
    ans = solu.sortedListToBST(solu, head)
    printtree.Pretty_print(ans)

