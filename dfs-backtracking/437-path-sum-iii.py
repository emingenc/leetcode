"""
https://leetcode.com/problems/path-sum-iii/

437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

Solution

preorder traversal
每次遍历将当前节点的值加到path数组里
从后往前遍历path数组，如果cur_sum == target，self.results += 1
再依次访问左节点右节点

"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        self.results = 0
        self.dfs(root, [], target)
        return self.results

    def dfs(self, node, path, target):
        if not node:
            return
        nums = path[:] + [node.val]
        n = len(nums)
        cur_sum = 0
        for i in range(n-1, -1, -1):
            cur_sum += nums[i]
            if cur_sum == target:
                self.results += 1
        self.dfs(node.left, path+[node.val], target)
        self.dfs(node.right, path+[node.val], target)
        return
