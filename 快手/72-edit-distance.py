"""
https://leetcode-cn.com/problems/edit-distance/

72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Solution:
- 在两个字符串前加空字符
- 而为动态规划
	- if word1[i] == word2[j]:
		- dp[i][j] = dp[i-1][j-1]
	- else:
		- dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = ' ' + word1[:], ' ' + word2[:]
        len1, len2 = len(word1), len(word2)
        dp = [[0]*len2 for _ in range(len1)]
        for i in range(len1):
            dp[i][0] = i
        for j in range(len2):
            dp[0][j] = j
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
