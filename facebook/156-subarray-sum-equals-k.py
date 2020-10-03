"""
https://leetcode.com/problems/subarray-sum-equals-k/


560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number 
of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Solution

遍历数组，累加当前数字且将当前和在字典的数字加1，如果当前和减去k已经存在则count加1
sum_dict[0] = 1

"""

import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        sum_dict = collections.defaultdict(int)
        sum_dict[0] = 1
        cur_sum = 0
        cnt = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_dict:
                cnt += sum_dict[cur_sum - k]
            sum_dict[cur_sum] += 1
        return cnt
