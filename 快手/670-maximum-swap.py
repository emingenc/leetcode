"""
https://leetcode-cn.com/problems/maximum-swap/

670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]


Solution:
-  将整数变成数组
-  对于每一个数 找到这个数后面的最大数
-  如果当前数小于这个最大数
-  找到这个最大数最后出现的位置 将其与当前数交换，停止

"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_copy = [int(i) for i in str(num)]
        n = len(num_copy)
        for i in range(n - 1):
            m = max(num_copy[i + 1:])
            if num_copy[i] < m:
                for j in range(n - 1, i, -1):
                    if num_copy[j] == m:
                        break
                num_copy[i], num_copy[j] = num_copy[j], num_copy[i]
                break
        return int("".join([str(i) for i in num_copy]))
