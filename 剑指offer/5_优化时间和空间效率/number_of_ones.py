"""
面试题32 从1到n整数中1出现的次数

要求：求从1到n整数的十进制表示中，1出现的次数

"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(0, n+1):
            temp = i
            while temp:
                if temp % 10 == 1:
                    count += 1
                temp /= 10
        return count
