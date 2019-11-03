"""
https://leetcode.com/problems/longest-common-prefix/

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

https://medium.com/@d_dchris/10-methods-to-solve-the-longest-common-prefix-problem-using-python-leetcode-14-a87bb3eb0f3a

"""


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for chars in strs:
                if char != chars[i]:
                    return shortest_str[0:i]

        return shortest_str
