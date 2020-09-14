"""
https://leetcode.com/problems/path-sum/

112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, root.val, sum)

    def dfs(self, node, cur_sum, target):
        if not node.left and not node.right:
            return cur_sum == target
        left = False
        if node.left:
            left = self.dfs(node.left, cur_sum + node.left.val, target)
        if left:
            return True
        if node.right:
            return self.dfs(node.right, cur_sum + node.right.val, target)
        return False
