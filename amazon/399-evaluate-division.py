"""
https://leetcode.com/problems/evaluate-division/

399. Evaluate Division

You are given equations in the format A / B = k, where A and B are variables 
represented as strings, and k is a real number (floating-point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries 
will result in no division by zero and there is no contradiction.


Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], 
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= equations[i][0], equations[i][1] <= 5
values.length == equations.length
0.0 <= values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0], queries[i][1] <= 5
equations[i][0], equations[i][1], queries[i][0], 
queries[i][1] consist of lower case English letters and digits.

"""

import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1.0 / value
        ans = [self.dfs(x, y, graph, set())
               if x in graph and y in graph else -1.0 for (x, y) in queries]
        return ans

    def dfs(self, x, y, graph, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in graph[x]:
            if n in visited:
                continue
            d = self.dfs(n, y, graph, visited)
            if d > 0:
                return d * graph[x][n]
        return -1.0
