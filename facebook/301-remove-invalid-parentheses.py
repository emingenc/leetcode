"""
https://leetcode.com/problems/remove-invalid-parentheses/

301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. 
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]


Solution

http://bookshadow.com/leetcode/

利用评价函数计算字符串中未匹配括号的个数
尝试从输入字符串中移除括号，若得到的新字符串的失配括号比原字符串少，则继续搜索；
否则剪枝。
calc函数统计字符串s中包含的失配括号数目。
变量n_left_more统计失配的左括号数目，
变量n_right_more统计失配的右括号数目。

"""

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calc(s):
            n_left_more = n_right_more = 0
            for c in s:
                n_left_more += {'(': 1, ')': -1}.get(c, 0)
                n_right_more += n_left_more < 0
                n_left_more = max(n_left_more, 0)
            return n_left_more + n_right_more

        visited = set([s])
        return dfs(s)
