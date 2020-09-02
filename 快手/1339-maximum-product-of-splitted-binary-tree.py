"""
https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree/

1339. Maximum Product of Splitted Binary Tree

Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:



Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:



Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1


Solution:

-  用后续遍历计算所有子树和，并同时计算整棵树的和
-  遍历所有子树，求最大乘积：
	-  max_prod = -float('inf')
      for subtree_sum in subtree_sums:
					max_prod = max(max_prod, (tree_sum - subtree_sum) * subtree_sum)
        
Time comlexity: 
In-order, Pre-order, and Post-order traversals are Depth-First traversals.
For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.
Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).
Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree, the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.
The complexity then becomes O(n + n-1), which is O(n).

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10**9 + 7
        subtree_sums = []
        tree_sum = self.dfs(root, subtree_sums)
        max_prod = -float('inf')
        for subtree_sum in subtree_sums:
            max_prod = max(max_prod, (tree_sum - subtree_sum) * subtree_sum)
        return max_prod % MOD

    def dfs(self, root, subtree_sum):
        if not root:
            return 0
        l = self.dfs(root.left, subtree_sum)
        r = self.dfs(root.right, subtree_sum)
        tree_sum = l + r + root.val
        subtree_sum.append(tree_sum)
        return tree_sum
