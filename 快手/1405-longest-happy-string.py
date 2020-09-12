"""
https://leetcode-cn.com/problems/longest-happy-string/

1405. Longest Happy String

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

Solution

- 循环每次输出字符长度减1
	- 将字符字典按照次数从大到小排列
	- 循环字典 每次取出一个字符 判断是否可以加入字符串 如果可以加入则加入到输出字符串
	- 每次加入完字典内字符数减1
	- 循环到输出字符串长度等于 a的次数 + b的次数 + c的次数
	- 如果循环字典时没有一个字符可以加入则调出函数

"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [[a, "a"], [b, "b"], [c, "c"]]
        total = a + b + c
        res = ""
        while total:
            d.sort(reverse=True)
            added = False
            for i, (count, char) in enumerate(d):
                if count == 0:
                    continue
                if self.canAdd(res, char):
                    res += char
                    d[i][0] -= 1
                    total -= 1
                    added = True
                    break
            if not added:
                break
        return res

    def canAdd(self, res, x):
        return len(res) < 2 or not (res[-1] == x and res[-2] == x)
