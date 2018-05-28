from leetcode.tree import printtree


class TreeNode:
    def __init__(self, val):
        self.val = val;
        self.left = None;
        self.right = None;

balance = 0
def insert(root, val):
    if root is None:
        root = TreeNode(val);
    else:
        if val < root.val:
            root.left = insert(root.left, val);  # 递归地插入元素
        elif val > root.val:
            root.right = insert(root.right, val);
    return root;


def query(root, val):
    # 如果搜到，返回ptr; 否则返回None
    ptr = root

    # 使用栈，非递归
    while ptr:
        if ptr.val == val:
            return True
        if ptr.val > val:
            ptr = ptr.left
        if ptr.val < val:
            ptr = ptr.right
    return False


def findmin(root):
    if root.left:
        return findmin(root.left);
    else:
        return root;


def delnum(root, val):
    if root is None:
        return;
    if val < root.val:
        return delnum(root.left, val);
    elif val > root.val:
        return delnum(root.right, val);
    else:  # 删除要区分左右孩子是否为空的情况
        if (root.left and root.right):

            tmp = findmin(root.right);  # 找到后继结点
            root.val = tmp.val;
            root.right = delnum(root.right, val);  # 实际删除的是这个后继结点

        else:
            if root.left is None:
                root = root.right;
            elif root.right is None:
                root = root.left;
    return root;


if __name__ == "__main__":
    # 测试代码
    root = TreeNode(3)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 8)
    # print("删除节点前")
    printtree.Pretty_print(root)
    # # print query(root,3);
    # print
    print(query(root, 1))
    # root = delnum(root, 1);
    # print
    # query(root, 1);
    # print("删除节点后")
    # printtree.Pretty_print(root)