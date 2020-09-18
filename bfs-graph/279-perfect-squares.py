"""
https://leetcode.com/problems/perfect-squares/

279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Solution

将小于n的square number加到数组squares
用bfs每次弹出一个数字和相对应的step，遍历所有square，
判断当前数字加上square是不是等于n是的话输出结果，否则将step+1和当前数与square的和加到队列。

"""


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 1
        i = 1
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        # while i*i <= n:
        #    squares.append(i*i)
        #    i += 1
        squares = squares[::-1]
        visited = set()
        queue = [(0, 0)]
        while queue:
            x, step = queue.pop(0)
            for y in squares:
                t = x + y
                if t < n and t not in visited:
                    queue.append((t, step + 1))
                    visited.add(t)
                if t == n:
                    return step + 1
        return -1
