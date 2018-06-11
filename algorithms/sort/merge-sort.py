# https://en.wikipedia.org/wiki/Merge_sort

"""
Class	Sorting algorithm
Data structure	                  Array
Worst-case performance	          O(n log n)
Best-case performance	          O(n log n) typical, O(n) natural variant
Average performance	              O(n log n)
Worst-case space complexity	      О(n) total with O(n) auxiliary, O(1) auxiliary with linked lists[1]
"""


# https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)