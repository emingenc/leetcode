"""
面试题25 二叉树中和为某一值的路径
要求：输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径

深度优先搜索变形


https://blog.csdn.net/fuxuemingzhu/article/details/79621325

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        if not root:
            return res
        self.target = expectNumber
        self.dfs(root, res, [root.val])
        return res

    def dfs(self, root, res, path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, path + [root.right.val])
        return
