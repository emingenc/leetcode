"""
https://leetcode.com/problems/next-greater-element-i/

496. Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 
where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number 
    for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, 
    so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, 
    so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            index = -1
            for i, num2 in enumerate(nums2):
                if num1 == num2:
                    index = i
                    break
            while index < len(nums2) and num1 >= nums2[index]:
                index += 1
            if index == len(nums2):
                ans.append(-1)
            else:
                ans.append(nums2[index])
        return ans


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = dict(), list()
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)
        return [dic.get(i, -1) for i in nums1]
