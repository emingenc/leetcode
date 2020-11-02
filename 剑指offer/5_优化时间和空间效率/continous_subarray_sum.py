"""
面试题31 连续子数组的最大和


"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        currSum, maxSum = 0, float('-inf')
        for num in array:
            currSum = num + currSum
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum
