"""
https://leetcode.com/problems/word-search/

79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

Solution

回溯
每次dfs完之后要把visited((x,y)) 变成False

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, visited):
                    return True
        return False

    def dfs(self, board, x, y, word, visited):
        if not word:
            return True
        if not self.isValid(x, y, board, visited) or word[0] != board[x][y]:
            return False
        visited.add((x, y))
        for delta_x, delta_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if self.dfs(board, x + delta_x, y + delta_y, word[1:], visited):
                return True
        visited.remove((x, y))
        return False

    def isValid(self, x, y, board, visited):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited
