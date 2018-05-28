# https://en.wikipedia.org/wiki/Merge_sort

# A sorting algorithm is said to be stable if two objects with equal keys appear in the same order
# in sorted output as they appear in the input array to be sorted.
# Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, etc.
# And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.
#
# Background: a "stable" sorting algorithm keeps the items with the same sorting key in order.
# Suppose we have a list of 5-letter words:
#
# peach
# straw
# apple
# spork
#
# If we sort the list by just the first letter of each word then a stable-sort would produce:
#
# apple
# peach
# straw
# spork

# In an unstable sort algorithm, straw or spork may be interchanged, but in a stable one,
# they stay in the same relative positions
# (that is, since straw appears before spork in the input, it also appears before spork in the output).
#

# https://en.wikipedia.org/wiki/Sorting_algorithm
# Quicksort is usually done in-place with O(log n) stack space
# Method: Merging
# Best: O(nlogn)
# Average: O(nlogn)
# Worst: O(nlogn)
# Memory: n
# Stable: yes


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