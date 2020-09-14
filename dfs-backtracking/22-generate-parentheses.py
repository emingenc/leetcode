"""
https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self._parenthesis('', n, n, res)
        return res

    def _parenthesis(self, comb, n_left, n_right, result):
        if n_left == 0 and n_right == 0:
            result.append(comb)
            return
        if n_left > 0:
            self._parenthesis(comb + '(', n_left - 1, n_right, result)
        if n_left < n_right:
            self._parenthesis(comb + ')', n_left, n_right - 1, result)
        return
