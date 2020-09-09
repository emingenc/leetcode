"""
https://leetcode.com/problems/find-median-from-data-stream/

295. Find Median from Data Stream

Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

Solution

max heap -> min heap
建一个min heap 一个max heap
每次加一个数如果min和max长度相同，则将数取负数加到max然后从max里弹出最大的乘以-1加入到min
如果min,max长度不同，将当前数加到min然后从min弹出最小元素乘以-1加到max

"""

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # the larger half of the list, min heap
        self.min_heap = []
        # the smaller half of the list, max heap (invert min-heap)
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, -
                           heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -
                           heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return float(self.min_heap[0])
