"""
面试题23 从上往下打印二叉树

思路：广度优先搜索，按层次遍历

"""


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return None
    queue = [root]
    res = []
    while queue:
        for _ in len(queue):
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res
