"""
https://leetcode.com/problems/graph-valid-tree/

261. Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to check 
whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0,1] is the same as [1,0] and 
thus will not appear together in edges.


Solution

无环且联通
建立图, 将第一个节点加入队列
bfs遍历队列，每次弹出一个节点如果已经访问过这个节点则返回false
将这个节点加入到visited
将当前节点的邻居节点加入queue，并且从图将邻居节点到当前节点边删除
最后将当前节点从图里删除
最后如果图不为空则说明不是树

"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # return n == len(edges) + 1
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        queue = [list(graph.keys())[0]]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
                graph[neighbor].remove(node)
            graph.pop(node)
        return not graph
