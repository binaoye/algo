# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: huffman.py
@time:2020-04-23 15:13
@file_desc: 
"""
import logging as log
import sys

log.basicConfig(level=log.DEBUG)
_logger = log.getLogger(__name__)
from leetcode.tree import printtree


class TreeNode(object):
    def __init__(self, x, flag=True):
        self.val = x
        self.left = None
        self.right = None
        self.encodes = ""
        self.is_node = flag

    def add_code(self, code='0'):
        self.encodes = code + self.encodes
        if self.left:
            self.left.add_code(code)
        if self.right:
            self.right.add_code(code)


class HuffmanTree(object):
    def __init__(self):
        self.root = None

    # 建立Huffman树
    def build(self, nums=[]):
        if len(nums) == 0:
            return
        node_list = []
        d = {}
        for i in nums:
            nd = TreeNode(i)
            node_list.append(nd)
            d[i] = nd
        # print(node_list)
        print('----')
        print(nums)
        for n in node_list:
            print(n.val)
        print("----")
        while(len(node_list)>1):
            node_list = sorted(node_list, key=lambda x: x.val, reverse=True)
            node = TreeNode(node_list[-1].val+node_list[-2].val, flag=False)
            node.left = node_list[-1]
            node.right = node_list[-2]
            node.left.add_code('0')
            node.right.add_code('1')
            node_list.pop()
            node_list.pop()
            node_list.append(node)

        for k in d.keys():
            print(k, "---", d[k].encodes)
        return node_list[0]


if __name__ == '__main__':
    nums = [5,8,4,11,9,13]
    # print(nums[-2])
    # print(sorted(nums, reverse=True))
    # nums.remove(nums[2])
    # print(nums)

    tree = HuffmanTree
    ans = tree.build(tree, nums)
    printtree.Pretty_print(ans)
    # node_list = []
    # for i in nums:
    #     node_list.append(TreeNode(i))
    # node_list = sorted(node_list, key=lambda x: x.val)
    # for node in node_list:
    #     print(node.val)