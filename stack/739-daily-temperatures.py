"""
https://leetcode.com/problems/daily-temperatures/

739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].


Solution 

我们这里的问题就是要找到大于当前元素的第一个元素的位置
直接建立一个非严格单调递减的栈，当我们碰到一个元素大于栈顶元素的时候，
我们知道此时这个元素一定是离栈顶元素最近的那个最大值的点，我们只要测试记录两者之间的位置距离就好了

"""

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
