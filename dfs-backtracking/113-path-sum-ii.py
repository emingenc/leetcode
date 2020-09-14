"""
https://leetcode.com/problems/path-sum-ii/

113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        results = []
        self.dfs(root, [], results, target)
        return results

    def dfs(self, node, path, results, target):
        if not node.left and not node.right:
            if sum(path) + node.val == target:
                results.append(path+[node.val])
            return
        if node.left:
            self.dfs(node.left, path+[node.val], results, target)
        if node.right:
            self.dfs(node.right, path+[node.val], results, target)
        return
