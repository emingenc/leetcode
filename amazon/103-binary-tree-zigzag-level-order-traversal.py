"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


Solution

bfs queue每个元素包括树的节点和当前层数

"""

from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = [(root, 0)]
        while queue:
            res.append([])
            for _ in range(len(queue)):
                cur, level = queue.pop(0)
                if cur:
                    if level % 2 == 0:
                        res[level].append(cur.val)
                    else:
                        res[level].insert(0, cur.val)
                    queue.append((cur.left, level + 1))
                    queue.append((cur.right, level + 1))
        return res[:-1]
