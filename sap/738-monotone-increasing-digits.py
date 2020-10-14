"""
738. Monotone Increasing Digits

Given a non-negative integer N, 
find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits 
if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].


Solution

case 1:
对于 14267 , 第一个出现下降的位置是4，所以把4变成3，把4后面的数字全部改成9.得到13999；

case 2:
对于1444267, 第一个降序的位置是最后一个4，如果只把最后一个4按照case1处理，那么得到的是1443999，仍然不满足题意。所以需要找到第一个位置的4，然后做case1操作，这样得到的是1399999。

从右到左找到第一个下降的位置，保存这个数
从右到左找到第一个等于这个数的位置
将这个数减1，之后的所有数变成9...

"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        num = [int(n) for n in str(N)]
        n = len(num)
        ind = n - 1
        for i in range(n - 2, -1, -1):
            if num[i] > num[i + 1] or num[i] == num[ind]:
                ind = i
        if ind == n - 1:
            return N
        num[ind] -= 1
        for i in range(ind + 1, n):
            num[i] = 9
        return int("".join(map(str, num)))
