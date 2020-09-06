"""
https://leetcode.com/problems/partition-labels/

763. Partition Labels

A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible so 
that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

Solution:

Keep a sliding window, 
the end of the window is the max index of the last seen index of the letters in the window. 
When I meet the end, the window closed and update the size of the window and 
the start of the window.
建立一个字典，存放每次字符和字符在字符串的最后位置
遍历每次字符，更新最后位置，最后位置是最后位置和该字符最后位置的最大值
如果最后位置和当前位置一样，则把最后位置减去起始位置加入输出数组，起始位置为最后位置加1

"""

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(S)}
        start, end = 0, 0
        ans = []
        for i, c in enumerate(S):
            end = max(end, last_index[c])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans
