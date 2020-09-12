"""
https://leetcode.com/problems/design-tic-tac-toe/

348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?


Solution

建立两个数组 存放行，列的player1的棋子数
rows = [0] * n #每一行的棋子数
cols = [0] * n  #每一列的棋子数
建两个变量，存放两个对角线的player1的棋子数目
更新棋子数是根据player如果是1则加1否则减1
最后更具每行每列两个对角线的棋子数判断谁获胜

"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n         # store total sums by row
        self.cols = [0] * n         # store total sums by column
        # store total sums by diagonal i.e (row == col)
        self.diagonal = 0
        # store total sums by anti-diagonal i.e (row == n-col-1)
        self.anti_diagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        value = 1 if player == 1 else -1

        self.rows[row] += value
        self.cols[col] += value
        if row == col:
            self.diagonal += value
        if row == (self.n - 1) - col:
            self.anti_diagonal += value

        if self.rows[row] == -self.n or self.cols[col] == -self.n or self.anti_diagonal == -self.n or self.diagonal == -self.n:
            return 2
        if self.rows[row] == self.n or self.cols[col] == self.n or self.anti_diagonal == self.n or self.diagonal == self.n:
            return 1

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
