"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/

637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level 
in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. 
Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.

"""

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            row = []
            for _ in range(n):
                node = queue.pop(0)
                if not node:
                    continue
                row.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if row:
                res.append(sum(row) / float(len(row)))
        return res
