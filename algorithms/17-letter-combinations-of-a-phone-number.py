# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.


# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


# Fork from https://shenjie1993.gitbooks.io/leetcode-python/017%20Letter%20Combinations%20of%20a%20Phone%20Number.html

class Solution(object):
    digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result = []
        self.dfs(digits, "", result)
        return result

    def dfs(self, digits, current, result):
        if not digits:
            result.append(current)
            return
        for c in self.digit2letters[digits[0]]:
            self.dfs(digits[1:], current + c, result)


if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]