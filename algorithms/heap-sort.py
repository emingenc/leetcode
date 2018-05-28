# http://www.geekviewpoint.com/python/sorting/heapsort

# Fork from http://www.geekviewpoint.com/python/sorting/heapsort
# https://github.com/AnthonyDiGirolamo/algorithms-in-python/blob/master/heapsort.py


# Time Complexity of Solution:
#  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).

"""
 Approach:
#  Heap sort happens in two phases.
#
#  In the first phase, the array is transformed into a heap.
#  A heap is a binary tree where
#  1) each node is greater than each of its children
#  2) the tree is perfectly balanced
#  3) all leaves are in the leftmost position available.
#
#  In phase two the heap is continuously reduced to a sorted array:
#  1) while the heap is not empty
#  - remove the top of the head into an array
#  - fix the heap.
#  Heap sort was invented by John Williams not by B. R. Heap.
#
#  MoveDown:
#  The movedown method checks and verifies that the structure is a heap.
#
#  Technical Details:
#  A heap is based on an array just as a hashmap is based on an
#  array. For a heap, the children of an element n are at index
#  2n+1 for the left child and 2n+2 for the right child.
#
#  The movedown function checks that an element is greater than its
#  children. If not the values of element and child are swapped. The
#  function continues to check and swap until the element is at a
#  position where it is greater than its children.

"""

# Worst Case:    O(n log n)
# Best Case:     O(n log n)
# Average Case:  O(n log n)
# Memory: 1
# Stable: No
# Method: Selection

def heapsort(a):
    """Run heapsort on a list a
    >>> a = [32,46,77,4344564,7322,3,46,7,32457,7542,4,667,54,]
    >>> heapsort(a)
    >>> print(a)
    [3, 4, 7, 32, 46, 46, 54, 77, 667, 7322, 7542, 32457, 4344564]
    """

    heapify(a, len(a))
    end = len(a)-1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)

def heapify(a, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return

if __name__ == "__main__":
    import doctest
    doctest.testmod()