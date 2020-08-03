"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

from typing import List

DIRECT = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        cnt = 0
        visited = set()
        N, M = len(grid), len(grid[0])
        for i in range(N):
            for j in range(M):
                if not self.valid(i, j, grid, visited):
                    continue
                queue = [(i, j)]
                visited.add((i, j))
                cnt += 1
                while queue:
                    x, y = queue.pop(0)
                    for x_delta, y_delta in DIRECT:
                        x_new = x + x_delta
                        y_new = y + y_delta
                        if self.valid(x_new, y_new, grid, visited):
                            queue.append((x_new, y_new))
                            visited.add((x_new, y_new))
        return cnt

    def valid(self, x, y, grid, visited):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and (x, y) not in visited and grid[x][y] == '1'
