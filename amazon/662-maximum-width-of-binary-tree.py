"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
 

Constraints:

The given binary tree will have between 1 and 3000 nodes.

Solution

bfs queue存放树的节点和当前位置，位置从1开始
节点i的左节点位置是2i,右节点是2i+1
每层最大宽度是最左和最右位置差 + 1

For node at i'th position position of node.left will be 2*i 
and  node.right will be 2*i + 1. We traverse through the tree
and assign position to nodes. Width of a level is difference of 
positions between the leftmost and rightmost nodes in that level.

"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 0
        queue = [(root, 1)]
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, i = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2*i))
                if node.right:
                    queue.append((node.right, 2*i + 1))
        return max_width
