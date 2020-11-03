"""
面试题50 树中两个结点的最低公共祖先

要求：求普通二叉树中两个结点的最低公共祖先

方法一：先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        self.travser(root, parents)
        path = []
        while p:
            path.append(p)
            p = parents[p]
        while q:
            if q in path:
                return q
            q = parents[q]
        return q

    def travser(self, node, parents):
        if node.left:
            parents[node.left] = node
            self.travser(node.left, parents)
        if node.right:
            parents[node.right] = node
            self.travser(node.right, parents)
        return
