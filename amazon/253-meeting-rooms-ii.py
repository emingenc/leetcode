"""
https://leetcode.com/problems/meeting-rooms-ii/


253. Meeting Rooms II


Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition 
to get new method signature.


Solution

heap存放会议结束时间
遍历所有会议，如果当前会议开始时间晚于最早结束的会议，将最早结束会议的结束时间替换成当前会议结束时间
否则将当前会议结束时间加入heap

"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
