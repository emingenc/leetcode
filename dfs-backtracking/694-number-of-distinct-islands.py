"""
https://leetcode.com/problems/number-of-distinct-islands/

694. Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. 
An island is considered to be the same as another if and only if one island can be translated 
(and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.

"""

from typing import List

DIRECTION = {'u': [-1, 0], 'd': [1, 0], 'l': [0, -1], 'r': [0, 1]}


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited, islands = set(), set()
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    island = []
                    self.dfs(i, j, grid, island, visited)
                    islands.add(''.join(island))
        return len(islands)

    def dfs(self, x, y, grid, island, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited:
            visited.add((x, y))
            for name, delta in DIRECTION.items():
                island.append(name)
                self.dfs(x + delta[0], y + delta[1], grid, island, visited)
        return
