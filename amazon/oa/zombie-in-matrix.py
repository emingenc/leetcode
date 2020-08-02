"""
https://leetcode.com/discuss/interview-question/411357/

Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
int minHours(int rows, int columns, List<List<Integer>> grid) {
	// todo
}
Related problems:

https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/walls-and-gates/ (premium)
https://leetcode.com/problems/rotting-oranges/

"""


def minHour(rows, columns, grid):
    if not rows or not columns:
        return 0

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = [[i, j] for i in range(rows)
             for j in range(columns) if grid[i][j] == 1]
    time, cnt, target = 0, 0, rows * columns - len(queue)
    while queue:
        if cnt == target:
            return time
        n = len(queue)
        for _ in range(n):
            [i, j] = queue.pop(0)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    queue.append([ni, nj])
                    cnt += 1
        time += 1
    return -1


if __name__ == "__main__":
    for args in (
        (
            4,
            5,
            [[0, 1, 1, 0, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0]]
        ),

    ):
        print(*args)
        print(minHour(*args))
