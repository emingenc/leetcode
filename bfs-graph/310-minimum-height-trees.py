"""
https://leetcode.com/problems/minimum-height-trees/

310. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
where edges[i] = [ai, bi] indicates that there is an undirected edge between 
the two nodes ai and bi in the tree, you can choose any node of the tree as the root. 
When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called 
minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between 
the root and a leaf.

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

Solution

Similar to the BFS topological sort. 
Remove the leaves, update the degrees of inner vertexes. 
Then remove the new leaves. 
Doing so level by level until there are 2 or 1 nodes left. 

"""

from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        que = collections.deque(
            [u for u, neighbors in graph.items() if len(neighbors) == 1])

        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                u = que.popleft()
                for v in graph[u]:
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        que.append(v)

        return list(que)
