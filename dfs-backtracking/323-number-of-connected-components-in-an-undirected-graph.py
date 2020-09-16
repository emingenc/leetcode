"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find 
the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] 
and thus will not appear together in edges.

"""

from typing import List
import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        seen = set()

        def dfs(node):
            if node not in seen:
                seen.add(node)
                for neighbor in g[node]:
                    dfs(neighbor)
            return 1

        def bfs(q):
            for node in q:
                if node not in seen:
                    q += g[node]
                    seen.add(node)
            return 1

        # return sum(bfs([i]) for i in range(n) if i not in seen)
        return sum(dfs(i) for i in range(n) if i not in seen)
