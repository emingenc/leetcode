"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', 
in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.


Solution

遍历字符串, 用stack平衡(, )
如果是(则将它的位置加入到stack
如果是) 判断stack，如果不会空则pop, 否则在原来字符上去除) 
最后遍历stack将stack里的多余的(的位置清空

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            if ch == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        while stack:
            s_list[stack.pop()] = ''
        return ''.join(s_list)
