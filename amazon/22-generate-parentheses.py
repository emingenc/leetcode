"""
https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


https://stackoverflow.com/questions/37385964/time-complexity-for-combination-of-parentheses#:~:text=1%20Answer&text=The%20complexity%20of%20this%20code,of%20length%20n%20is%20created.

The complexity of this code is O(n * Cat(n)) where Cat(n) is the nth Catalan number. 
There are Cat(n) possible valid strings that are valid combinations of parenthesis 
(see https://en.wikipedia.org/wiki/Catalan_number), 
and for each a string of length n is created.

Since Cat(n) = choose(2n, n) / (n + 1), 
O(n * Cat(n)) = O(choose(2n, n)) = O(4^n / sqrt(n)) 
(see https://en.wikipedia.org/wiki/Central_binomial_coefficient).

https://leetcode.com/problems/generate-parentheses/discuss/10099/time-complexity-to-generate-all-combinations-of-well-formed-parentheses

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
