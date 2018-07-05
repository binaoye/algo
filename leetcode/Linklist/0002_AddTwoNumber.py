# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 遍历链表得到数字
        num1 = self.getNum(self,l1)
        num2 = self.getNum(self,l2)
        return self.createNum(self,num1+num2)



    def getNum(self,linkNode):
        num = ""
        if (linkNode.val != 0)&(type(linkNode)==ListNode):
            while linkNode is not None:
                num = str(linkNode.val) + num
                linkNode = linkNode.next
        if num != "":
            return int(num)
        else:
            return 0

    def createNum(self,num):
        print("calc",num)
        strnum = str(num)
        if num == 0:
            return ListNode(0)
        else:
            print(strnum[0])
            result = ListNode(int(strnum[0]))
            for i in range(len(strnum)-1):
                print("now:",strnum[i+1])
                node = ListNode(int(strnum[i+1]))
                node.next = result
                result = node
        return result


if __name__ == "__main__":
    rootnode = ListNode(5)
    node1 = ListNode(8)
    node2 = ListNode(1)
    rootnode.next = node1
    node1.next = node2
    solu = Solution

    line1 = ListNode(2)
    line2 = ListNode(4)
    line3 = ListNode(3)
    line1.next = line2
    line2.next = line3
    print(solu.getNum(solu,solu.addTwoNumbers(solu,line1,rootnode)))
