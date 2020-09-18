"""
https://leetcode.com/problems/walls-and-gates/

286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  
Solution

找出所有为0的位置，放入队列中
从为0的位置开始向四个方向遍历，直接修改迷宫的可以走的位置的数字是距离门最近的距离
把新的可以走的位置放入队列中，继续搜索

"""

from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        n, m = len(rooms), len(rooms[0])
        q = [(i, j, 1) for i in range(n) for j in range(m) if not rooms[i][j]]
        while q:
            # for _ in range(len(q)):
            i, j, dist = q.pop(0)
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and rooms[x][y] == 2**31 - 1:
                    rooms[x][y] = dist
                    q.append((x, y, dist + 1))
        return
