"""
https://leetcode.com/problems/word-break-ii/

140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        https://leetcode.com/problems/word-break-ii/discuss/44258/Python-DFS-solution-O(mn*n)-running-time
        #running time: O(mn^2), n = len(s), m = len(wordDict)
        Let‘s say the average word length in wordDict is k, so it takes n/k times to reach end.
        Each time, the helper function would be called and it's running time is O(m*n)
        So the whole runinng time  would be O( m*n*n/k), which is O(m*n^2)
        """
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if not s:
            return [None]
        if s in memo:
            return memo[s]
        res = []
        for word in wordDict:
            n = len(word)
            if word == s[:n]:
                for each in self.dfs(s[n:], wordDict, memo):
                    if each:
                        res.append(word + " " + each)
                    else:
                        res.append(word)
        memo[s] = res
        return res
