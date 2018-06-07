# https://leetcode.com/problems/permutations/description/

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

# Fork from https://github.com/twtrubiks/leetcode-python/blob/master/046%20Permutations.py

class Solution(object):
    def permute(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(num) == 0: return []
        if len(num) == 1: return [num]

        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i + 1:]):
                res.append([num[i]] + j)

        return res


if __name__ == "__main__":
    my_nums = [1, 2, 3]
    print("Original Cofllection: ", my_nums)
    print("Collection of distinct numbers:\n", Solution().permute(my_nums))

