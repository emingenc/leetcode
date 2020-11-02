"""
面试题20 顺时针打印矩阵
每一圈的开始位置总是坐上角元素[0, 0], [1, 1]

"""


def printMatrix(matrix):
    out = []
    while matrix:
        # 上边界即为数组的第一个子数组
        out += matrix.pop(0)
        # 如果这里仅判断if matrix，那么对于测试数组例[[1],[2],[3]]，循环后变成了[[],[]]，matrix不为空
        if matrix and matrix[0]:
            # 右边界即为数组每一项的最后一个元素
            for row in matrix:
                out.append(row.pop())
        # 下边界即为数组最后一个子数组的逆序排列
        if matrix:
            out += matrix.pop()[::-1]
        if matrix and matrix[0]:
            # 左边界即为数组从尾到头的每一项子数组的第一个元素
            for row in matrix[::-1]:
                out.append(row.pop())
    return out


def print_matrix(matrix):
    """
    :param matrix: [[]]
    """
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    return ret


def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1  # 最后一行
    col = cols - start - 1
    # left->right
    for c in range(start, col+1):
        ret.append(matrix[start][c])
    # top->bottom
    if start < row:
        for r in range(start+1, row+1):
            ret.append(matrix[r][col])
    # right->left
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom->top
    if start < row and start < col:
        for r in range(start+1, row)[::-1]:
            ret.append(matrix[r][start])


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(printMatrix(matrix))
