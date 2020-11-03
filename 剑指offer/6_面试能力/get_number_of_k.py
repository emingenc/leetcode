"""
面试题38 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。

思路: 使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减

"""


class Solution:
    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data)-1
        leftk = self.getleftK(data, k, left, right)
        rightk = self.getrightK(data, k, left, right)
        return rightk - leftk + 1

    def getleftK(self, data, k, left, right):
        while left <= right:
            middle = (left+right)//2
            if data[middle] < k:
                left = middle + 1
            else:
                right = middle - 1
        return left

    def getrightK(self, data, k, left, right):
        while left <= right:
            middle = (left+right)//2
            if data[middle] <= k:
                left = middle + 1
            else:
                right = middle - 1
        return right
