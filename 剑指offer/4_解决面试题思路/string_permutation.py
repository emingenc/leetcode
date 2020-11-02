"""
面试题28 字符串的排列
要求：求输入字符串的全排列

思路：递归完成，也可以直接使用库函数

题目描述：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

"""


class Solution:
    def permutation(self, source):
        if not source:
            return []
        res = []
        self._permutation(source, res, '', len(source))
        return sorted(list(set(res)))

    def _permutation(self, source, res, path, n):
        if len(path) == n:
            res.append(path)
            return
        for i in range(len(source)):
            self._permutation(source[:i] + source[i+1:],
                              res, path + source[i], n)
