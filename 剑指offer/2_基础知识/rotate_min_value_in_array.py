"""
https://github.com/JushuangQiao/Python-Offer/tree/master/second/fourth

面试题8 旋转数组的最小数字
要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]

思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找

"""


def find_min(nums):
    if not nums:
        return False
    left, right = 0, len(nums) - 1
    while nums[left] >= nums[right]:
        mid = left + (right - left) // 2
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[0]
