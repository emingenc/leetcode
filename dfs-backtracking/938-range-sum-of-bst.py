"""
https://leetcode.com/problems/range-sum-of-bst/

938. Range Sum of BST

Given the root node of a binary search tree, 
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        self.cur_sum = 0
        self.dfs(root, L, R)
        return self.cur_sum

    def dfs(self, root, L, R):
        if not root:
            return
        if L <= root.val <= R:
            self.cur_sum += root.val
        if root.val > L:
            self.dfs(root.left, L, R)
        if root.val < R:
            self.dfs(root.right, L, R)
        return
