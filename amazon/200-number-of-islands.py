"""
https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 
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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = set()
        n_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not self.isValid(i, j, grid, visited):
                    continue
                queue = [(i, j)]
                visited.add((i, j))
                n_islands += 1
                while queue:
                    x, y = queue.pop(0)
                    for x_delta, y_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x_new = x + x_delta
                        y_new = y + y_delta
                        if self.isValid(x_new, y_new, grid, visited):
                            queue.append((x_new, y_new))
                            visited.add((x_new, y_new))
        return n_islands

    def isValid(self, x, y, grid, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == '1'
