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
