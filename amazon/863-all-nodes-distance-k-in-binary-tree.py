"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

Solution

- DFS建立一个邻接矩阵
- 在这个邻接矩阵上使用BFS

Complexity

https://stackoverflow.com/questions/9844193/what-is-the-time-and-space-complexity-of-a-breadth-first-and-depth-first-tree-tr

BFS:

Time complexity is O(|V|), where |V| is the number of nodes. You need to traverse all nodes.
Space complexity is O(|V|) as well - since at worst case you need to hold all vertices in the queue.

DFS:

Time complexity is again O(|V|), you need to traverse all nodes.
Space complexity - depends on the implementation, 
a recursive implementation can have a O(h) space complexity [worst case], 
where h is the maximal depth of your tree.
Using an iterative solution with a stack is actually the same as BFS, 
just using a stack instead of a queue - so you get both O(|V|) time and space complexity.

(*) Note that the space complexity and time complexity is a bit different for a tree 
than for a general graphs becase you do not need to maintain a visited set for a tree, 
and |E| = O(|V|), so the |E| factor is actually redundant.
"""

from typing import List
import collections


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # dfs
        graph = collections.defaultdict(list)

        def dfs(par, cur):
            if par and cur:
                graph[par.val].append(cur.val)
                graph[cur.val].append(par.val)
            if cur.left:
                dfs(cur, cur.left)
            if cur.right:
                dfs(cur, cur.right)
            return
        dfs(None, root)
        # bfs
        queue = [target.val]
        visited = set([target.val])
        for _ in range(K):
            for _ in range(len(queue)):
                node = queue.pop(0)
                for child in graph[node]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
        return list(queue)
