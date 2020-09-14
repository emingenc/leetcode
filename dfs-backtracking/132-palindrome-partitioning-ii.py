"""
https://leetcode.com/problems/palindrome-partitioning-ii/

132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.


DP definition:
dp[i] is the mininum cuts needed for a palindrome partition of s[: i], 1 <= i <= len(s).

Optimal substructure:
dp[j] = min(dp[i - 1] + 1) for 1 <= i <= j if s[i - 1: j] is panlindrome.

Base case:
dp[1] = 0. For convenience, let dp[0] = -1.

"""


class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [(i-1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                temp = s[j:i]
                if temp[:] == temp[::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
