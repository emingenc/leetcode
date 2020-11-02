"""
面试题36 数组中的逆序对
要求：在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数

思路: 归并排序,先把数组依次拆开，然后合并的时候统计逆序对数目，并排序

https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/bao-li-jie-fa-fen-zhi-si-xiang-shu-zhuang-shu-zu-b/

"""

from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 0
        res = 0
        for i in range(0, size - 1):
            for j in range(i + 1, size):
                if nums[i] > nums[j]:
                    res += 1
        return res


class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        与归并排序相比只有几处改动        
        '''
        def merge(left, right):
            # left = [5, 7]
            # right = [4, 6]
            temp = [0]*(len(left)+len(right))
            i, j, ind = 0, 0, 0
            count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp[ind] = left[i]
                    i += 1
                else:
                    temp[ind] = right[j]
                    j += 1
                    # 改动4 只有在左侧数字大于右侧时，才会出现逆序对，数目为len(left)-i，
                    # 因为left是一个升序数组，一旦第i个数大于右侧，i~end的所有数字都满足逆序对
                    count += len(left)-i
                ind += 1
            if i == len(left):
                temp[ind:] = right[j:]
            else:
                temp[ind:] = left[i:]
            return temp, count

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums)//2
            # 改动1 返回左侧数组内部逆序对个数leftcount # [5, 7], 1
            left, leftcount = merge_sort(nums[:mid])
            # 改动2 返回右侧数组内部逆序对个数rightcount # [4, 6], 1
            right, rightcount = merge_sort(nums[mid:])

            # 改动3 返回左右两侧数组共同组成的逆序对个数count # [4, 5, 6, 7], 3
            temp, count = merge(left, right)
            return temp, count + leftcount + rightcount

        return merge_sort(nums)[1]
