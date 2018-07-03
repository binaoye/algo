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


def balanceAndInsert(root, val):
    node = TreeNode(val)
    if root is None:
        return node
    if root.val > val:
        root.left = balanceAndInsert(root.left, val)
    elif root.val < val:
        root.right = balanceAndInsert(root.right, val)
    lh = getHeight(root.left)
    rh = getHeight(root.right)
    balance = lh -rh
    print('balance', balance, 'insert', val)
    if balance > 1:
        if root.left.left is not None:
            # 左单旋ll
            nnode = lltransform(root)
            return nnode
        elif root.left.right is not None:
            # lr
            nnode = lrtransform(root)
            return nnode
    if balance < -1:
        if root.right.right is not None:
            nnode = rrtransform(root)
            return nnode
            # 右单旋
        elif root.left.right is not None:
            # rl
            nnode = rltransform(root)
            return nnode

    return root

def lltransform(root):
    print("Before ll")
    printtree.Pretty_print(root)
    nnode = root.left
    root.left = None
    nnode.right = root
    print("After ll")
    printtree.Pretty_print(nnode)
    return nnode

def lrtransform(root):
    print("Before lr")
    printtree.Pretty_print(root)
    midnode = root.left
    leftnode = midnode.right
    midnode.left = leftnode
    midnode.right = root

    print("After lr")
    printtree.Pretty_print(midnode)
    return midnode

def rrtransform(root):
    print("Before rr")
    printtree.Pretty_print(root)
    nnode = root.right
    root.right = None
    nnode.left = root
    print("After rr")
    printtree.Pretty_print(nnode)
    return nnode

def rltransform(root):
    print("Before rl")
    printtree.Pretty_print(root)
    rightnode = root.right
    midnode = rightnode.left
    midnode.left = root
    midnode.right = rightnode
    print("After rl")
    printtree.Pretty_print(midnode)
    return midnode

def getHeight(root):
    # 递归出口
    if root is None:
        return 0
    lh = getHeight(root.left)
    rh = getHeight(root.right)
    return max(lh, rh) + 1

if __name__ == "__main__":
    # 测试代码
    root = TreeNode(3)
    root = balanceAndInsert(root, 2)
    root = balanceAndInsert(root, 1)
    root = balanceAndInsert(root, 2)
    root = balanceAndInsert(root, 4)
    root = balanceAndInsert(root, 3)
    root = balanceAndInsert(root, 5)
    root = balanceAndInsert(root, 7)
    root = balanceAndInsert(root, 8)
    root = balanceAndInsert(root, 10)
    root = balanceAndInsert(root, 6)
    root = balanceAndInsert(root, 11)
    root = balanceAndInsert(root, 12)
    root = balanceAndInsert(root, 13)
    root = balanceAndInsert(root, 14)
    root = balanceAndInsert(root, 15)
    root = balanceAndInsert(root, 16)
    root = balanceAndInsert(root, 18)
    root = balanceAndInsert(root, 19)
    root = balanceAndInsert(root, 20)
    root = balanceAndInsert(root, 21)
    root = balanceAndInsert(root, 22)
    root = balanceAndInsert(root, 23)
    root = balanceAndInsert(root, 24)
    root = balanceAndInsert(root, 25)
    root = balanceAndInsert(root, 26)
    root = balanceAndInsert(root, 27)
    root = balanceAndInsert(root, 28)
    root = balanceAndInsert(root, 29)
    root = balanceAndInsert(root, 30)
    root = balanceAndInsert(root, 31)
    root = balanceAndInsert(root, 32)
    # print("删除节点前")
    printtree.Pretty_print(root)
    # # print query(root,3);
    # print
    print(query(root, 1))
    print(getHeight(root))
    # root = delnum(root, 1);
    # print
    # query(root, 1);
    # print("删除节点后")
    # printtree.Pretty_print(root)