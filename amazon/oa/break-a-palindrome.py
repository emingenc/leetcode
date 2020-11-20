"""
1328. Break a Palindrome

https://leetcode.com/problems/break-a-palindrome/


Given a palindromic string palindrome, 
replace exactly one character by any lowercase English letter so that the string 
becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string. 
If there is no way to do so, return the empty string.

Example 1:

Input: palindrome = "abccba"

Output: "aaccba"

Example 2:

Input: palindrome = "a"

Output: ""

Constraints:

1 <= palindrome.length <= 1000

palindrome consists of only lowercase English letters.


https://leetcode.com/problems/break-a-palindrome/discuss/846873/Python-3-or-Greedy-one-pass-or-Explanations

"""

"""
Explanation

If length of palindrome == 1, return ''

For even length string, if we found a char that is not a, replace it with a and return

For odd length string, if we find a char that is not a and it's not the middle of string, 
replace it with a and return

If all a in the string, replace the last char to b

"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        for i, c in enumerate(palindrome):
            if c != 'a' and ((i != n // 2 and n % 2) or not n % 2):
                return palindrome[:i] + 'a' + palindrome[i+1:]
        else:
            return palindrome[:-1] + 'b'
