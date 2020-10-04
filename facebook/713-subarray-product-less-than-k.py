"""
https://leetcode.com/problems/subarray-product-less-than-k/

713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements 
in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: 
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

Solution
双指针方法

"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # (product of the elements in the window, left window index)
        status = (1, 0)
        result = 0
        for right, num in enumerate(nums):
            product, left = status
            product *= num
            while product >= k and left < right + 1:
                product /= nums[left]
                left += 1
            status = (product, left)
            result += right - left + 1
        return result
