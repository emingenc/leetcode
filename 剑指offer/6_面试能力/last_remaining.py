"""
面试题45 圆圈中最后剩下的数字

要求：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数

思路：当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0，关键是推导出关系表达式

"""


def last_num(n, m):
    ret = 0
    if n == 1:
        return 0
    for i in range(2, n + 1):
        ret = (m + ret) % i
    return ret


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        pos = 0
        for i in range(2, n + 1):
            pos = (pos + m) % i
        return pos
