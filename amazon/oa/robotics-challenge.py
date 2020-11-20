"""
### Robotics Challenge

Several teams across Amazon are participating in a company-wide robotics challenge. Your team has programmed a robot to play a game in which it throws a ball at various blocks marked with a symbol so as to knock these out. You have been asked to automate the scoring process. A score is computed for each throw. The "last score" is the score of the previous throw (or 0, if there is no previous throw) and the total score is the sum of the scores of all the throws. the symbol on a block can be an integer, a sign or a letter. Each sign or letter represents a special rule as given below:

- If a throw hits a block with an integer, the score for that throw is the value of that integer.
- If a throw hits a block with an X, the score for that throw is double the last score.
- If a throw hits a block with +, the score for that throw is the sum of the last two scores.
- If a throw hits a block with a Z, the last score is removed, as though the last throw never happened. Its value does not count towards the total score, and the subsequent throws will ignore it when computing their values.

Write an algorithm that computes the total score for a given list of ordered hits by the robot.

Input

The input to the function/method consists of two arguments -
num, an integer representing the number of symbols in the list;
blocks, the list of strings representing symbols of the list;

Output

Return an integer representing the total score for the given list of ordered hits.

Examples

Input:

num = 8

blocks = [5, -2, 4, Z, X, 9, +, +]

Expected Return Value: 27

Explanation:

i = 0, total score 5;

i = 1, total score 5 + -2 = 3;

i = 2, total score 3 + 4 = 7;

i = 3, total score 7 - 4 = 3 (with 'Z' previous throw is removed from scores.)

i = 4, total score 3 + (-2 * 2) = -1 (with 'X', we multiply last score by 2. notice that 4 is removed in i = 3, we skip it through )

i = 5, total score -1 + 9 = 8;

i = 6, total score 8 + (-4 + 9) = 13

i = 7, total score 13 + (9 + 5) = 27

Input:

num = 4

blocks = [1, 2, +, Z]

Expected Return Value: 3


https://leetcode.com/problems/baseball-game/description/


682. Baseball Game


You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1"]
Output: 1
 

Constraints:

1 <= ops.length <= 1000
ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.


"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
