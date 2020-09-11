"""
https://leetcode.com/problems/sliding-puzzle/

773. Sliding Puzzle


On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, 
and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. 
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

Solution

搜索返回步数用bfs
将二维数组状态转换成字符串
queue存放状态和步数
每次bfs，找到0的位置，按四个方向继续搜索 (将新位置和原来位置元素交换)，知道新的状态符合最终状态，每次结束搜索将0放回原来位置

"""

from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal = "123450"
        start = self.board2str(board)
        queue = [(start, 0)]
        visited = set()
        visited.add(start)
        while queue:
            state, step = queue.pop(0)
            if state == goal:
                return step
            pos_0 = state.index('0')
            x, y = pos_0 // 3, pos_0 % 3
            state = list(state)
            for delta_x, delta_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + delta_x, y + delta_y
                if not (0 <= new_x < len(board) and 0 <= new_y < len(board[0])):
                    continue
                state[new_x * 3 + new_y], state[x * 3 +
                                                y] = state[x * 3 + y], state[new_x * 3 + new_y]
                str_state = "".join(state)
                if str_state not in visited:
                    queue.append((str_state, step + 1))
                    visited.add(str_state)
                state[new_x * 3 + new_y], state[x * 3 +
                                                y] = state[x * 3 + y], state[new_x * 3 + new_y]
        return -1

    def board2str(self, board):
        str_board = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                str_board += str(board[i][j])
        return str_board
