"""
https://leetcode.com/problems/minimum-cost-to-connect-sticks/

1167. Minimum Cost to Connect Sticks

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
 

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4


"""

import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks:
            return 0
        min_cost = 0
        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)
        while len(heap) > 1:
            cost = heapq.heappop(heap) + heapq.heappop(heap)
            min_cost += cost
            heapq.heappush(heap, cost)
        return min_cost
