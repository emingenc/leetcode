"""
https://leetcode.com/problems/critical-connections-in-a-network/

1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections 
forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, 
will make some server unable to reach some other server.

Return all critical connections in the network in any order.


Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.


Solutions:

-通过用dfs访问孩子节点来更新当前节点的步数，如果当前节点步数能变小，则说明当前节点和孩子节点能构成环，否则是桥
-用dfs不断更新步数为当前节点和附近节点最小值
-如果有环的话当前节点的步数一定改变

Time complexity: O(V + E)
https://stackoverflow.com/questions/11468621/why-is-the-time-complexity-of-both-dfs-and-bfs-o-v-e

"""

import collections
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        res = []
        steps = [-1] * n
        self.dfs(graph, 0, -1, 0, steps, res)
        return res

    def dfs(self, graph, cur, par, level, steps, res):
        steps[cur] = level + 1
        for child in graph[cur]:
            if child == par:
                continue
            # if the child is not visited, then visite the child and update the step with min cur and child steps
            elif steps[child] == -1:
                steps[cur] = min(steps[cur], self.dfs(
                    graph, child, cur, level + 1, steps, res))
            # if the child is visited then update the step with the min of cur step and child's step
            else:
                steps[cur] = min(steps[cur], steps[child])
        if steps[cur] == level + 1 and par != -1:
            res.append([par, cur])
        return steps[cur]
