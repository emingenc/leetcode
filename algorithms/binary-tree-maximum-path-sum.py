#Fork from https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-maximum-path-sum.py

# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#

# https://blog.csdn.net/qqxx6661/article/details/78484940

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self._maxPathSum(root)
        return self.maxSum

    def _maxPathSum(self, root):
        if root is None:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val