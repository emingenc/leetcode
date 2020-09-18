"""
https://leetcode.com/problems/shortest-distance-from-all-buildings/

317. Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. 
If it is not possible to build such house according to the above rules, return -1.


"""

from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, tot = len(grid), len(grid) and len(grid[0]), sum(
            1 for row in grid for col in row if col == 1)
        bld, dst = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]

        def bfs(i, j):
            seen, cnt, q = {(i, j)}, 1, [(i, j, 1)]
            while q:
                i, j, d = q.pop(0)
                # for i, j, d in q:
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x, y) not in seen:
                        seen.add((x, y))
                        if not grid[x][y]:
                            bld[x][y], dst[x][y] = bld[x][y] + 1, dst[x][y] + d
                            q.append((x, y, d+1))
                        else:
                            cnt += 1
            return cnt == tot

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not bfs(i, j):
                    return -1
        return min((dst[i][j] for i in range(m) for j in range(n) if not grid[i][j] and bld[i][j] == tot), default=-1)
