"""
https://leetcode.com/discuss/interview-question/436073/

You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

Output: [2, 3, 5]
Related problems:

Critical Connections
https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
https://cp-algorithms.com/graph/cutpoints.html


https://leetcode.com/discuss/interview-question/436073/

Solving Critical Connections in a Network helps cement the concept here.

Key Idea - For any edge parent -> child, 
if an edge exists between child -> ancestor where ancestor is an ancestor of the vertex parent, 
this is not a bridge edge.
In addition to the usual visited set during a DFS, you also keep track of discovered, 
which is the time when a particular node was first first seen. 
low is the minimum of the time the node was first seen and all its neighbors (expect for the parent) 
were first seen.
"""


import collections
from typing import List


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = collections.defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    # lowest link needed to find backedges
    low = {}
    discovered = collections.defaultdict(int)
    # edges that will break the connected components
    bridges = []

    def dfs(vertex, parent, time):
        visited.add(vertex)
        low[vertex] = time
        discovered[vertex] = time
        for child in graph[vertex]:
            if child == parent:
                continue
            if child not in visited:
                dfs(child, vertex, time+1)
                # Update the lowest link value
                # The lowest link of a node, is either its own value or the lowest link of all its neighbors
                # that are not the parent node
                low[vertex] = min(low[vertex], low[child])
                if discovered[vertex] < low[child]:
                    bridges.append([vertex, child])
            else:
                low[vertex] = min(low[vertex], discovered[child])

    # run dfs on the nodes at the top level
    for i in range(n):
        if i not in visited:
            dfs(i, None, 0)

    return sorted([bridge[0] for bridge in bridges])


if __name__ == "__main__":
    for args in (
        (
            7,
            [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        ),
    ):
        print('-----')
        print(*args)
        print('criticalConnections')
        print(criticalConnections(*args))
