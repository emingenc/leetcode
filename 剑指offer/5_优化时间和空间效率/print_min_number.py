"""
面试题33 把数组排成最小的数

要求：把数组中的值拼接，找出能产生的最小的数[321,32,3]最小的数是321323

思路: Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以

题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

解题思路
遇到这个题，全排列当然可以做，但是时间复杂度为O(n!)。在这里我们自己定义一个规则，对拼接后的字符串进行比较。

排序规则如下：

若ab > ba 则 a 大于 b，
若ab < ba 则 a 小于 b，
若ab = ba 则 a 等于 b；
根据上述规则，我们需要先将数字转换成字符串再进行比较，因为需要串起来进行比较。比较完之后，按顺序输出即可。

"""


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""

        def compare(a, b): return cmp(str(a) + str(b), str(b) + str(a))
        cur = sorted(numbers, cmp=compare)
        return int("".join(str(s) for s in cur))
