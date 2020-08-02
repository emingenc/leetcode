"""
https://www.lintcode.com/problem/minimum-cost-to-connect-sticks/description?_from=ladder&&fromId=156

https://www.jiuzhang.com/problem/minimum-cost-to-connect-sticks/

1872. Minimum Cost to Connect Sticks
Description
中文
English
You have some sticks with positive integer lengths.
You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y. 
You perform this action until there is one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.

1 <= sticks.length <= 10^41≤sticks.length≤10^4
​​ 
1 <= sticks[i] <= 10^41≤sticks[i]≤10^4
​​ 
Have you met this question in a real interview?  
Example
Example 1:

Input:
 [2,4,3]
Output: 14
Explanation: First connect 2 and 3 to 5 and cost 5; then connect 5 and 4 to 9; total cost is 14
Example 2:

Input:
 [1,8,3,5]
Output: 30

"""

import heapq


class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """

    def MinimumCost(self, sticks):
        # write your code here
        if not sticks:
            return 0

        queue = []  # 用来保持木棒的队列
        for n in sticks:
            heapq.heappush(queue, n)
        cost = 0
        for i in range(len(sticks)-1):  # 总共合并n-1次
            a = heapq.heappop(queue)
            b = heapq.heappop(queue)
            cost += (a+b)
            heapq.heappush(queue, (a+b))

        return cost
