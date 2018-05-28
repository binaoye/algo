# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def PrintLinklist(root):
    ret = []
    while root:
        ret.append(root.val)
        root = root.next
    print(ret)