"""
https://leetcode-cn.com/problems/number-of-closed-islands/

1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1


Solution:

- 用dfs删除top, bottom, left, right上的岛屿
- 在除去边缘的位置用dfs搜索岛屿数

Time Complexity: O(N*M) 
Auxiliary Space: O(N*M) 

"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        # remove the islands on top and bottom
        for i in range(m):
            if not grid[0][i]:
                self.dfs(0, i, grid, visited)
            if not grid[n - 1][i]:
                self.dfs(n - 1, i, grid, visited)
        # remove the islands on left and right
        for i in range(n):
            if not grid[i][0]:
                self.dfs(i, 0, grid, visited)
            if not grid[i][m - 1]:
                self.dfs(i, m - 1, grid, visited)
        # compute the number of closed islands
        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if not grid[i][j] and (i, j) not in visited:
                    ans += 1
                    self.dfs(i, j, grid, visited)
        return ans

    def dfs(self, i, j, grid, visited):
        visited.add((i, j))
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = i + dx, j + dy
            if self.isValid(x, y, grid, visited):
                self.dfs(x, y, grid, visited)

    def isValid(self, x, y, grid, visited):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and (x, y) not in visited and grid[x][y] == 0
