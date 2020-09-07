"""
https://leetcode.com/problems/minimum-time-difference/

539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, 
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

Solution

将时间转换成分钟
用zip(timePoints, timePoints[1:] + timePoints[:1])建立循环数组并且比较相邻元素差
相邻时间差要用%(24*60)

"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            time_list = time.split(':')
            return int(time_list[0]) * 60 + int(time_list[1])
        times = list(map(convert, timePoints))
        times.sort()
        return min((y - x) % (24 * 60) for x, y in zip(times, times[1:] + times[:1]))
