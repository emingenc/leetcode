"""
https://leetcode.com/problems/continuous-subarray-sum/

523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size 
at least 2 that sums up to a multiple of k, that is, 
sums up to n*k where n is also an integer.
 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

累加数组，并将当前和除以K的余数加到字典，每次判断当前和除以K的余数是否存在，
如果存在则当前位置和上一个位置的差大于2则返回True

seen[0] = -1

7 % 2 -> 1
9 % 2 -> 1
(9 - 7) % 2 -> 0

"""

import collections
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = collections.defaultdict(int)
        seen[0] = -1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if k != 0:
                cur_sum %= k
            if cur_sum in seen:
                if i - seen[cur_sum] >= 2:
                    return True
            else:
                seen[cur_sum] = i
        return False
