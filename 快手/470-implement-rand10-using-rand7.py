"""
https://leetcode-cn.com/problems/implement-rand10-using-rand7/

470. Implement Rand10() Using Rand7()

Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called while testing. 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
 

Example 1:

Input: n = 1
Output: [2]
Example 2:

Input: n = 2
Output: [2,8]
Example 3:

Input: n = 3
Output: [3,8,10]
 

Constraints:

1 <= n <= 105


"""

# The rand7() API is already defined for you.


def rand7():
    pass
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return self.rand40() % 10 + 1

    def rand49(self):
        """
        random integer in 0 ~ 48
        """
        return 7 * (rand7() - 1) + rand7() - 1

    def rand40(self):
        """
        random integer in 0 ~ 40
        """
        num = self.rand49()
        while num >= 40:
            num = self.rand49()
        return num
