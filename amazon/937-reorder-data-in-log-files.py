"""
https://leetcode.com/problems/reorder-data-in-log-files/

937. Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

Solution

建两个数组 一个存放数字log 一个存放字母log
对于每个数字log，转换成一个tuple存放入数字数组，tuple的一个元素是log本身，另一个元素是log的头
对tuple排序，根据log的内容，然后是log头
最后将排好序的字母数组与数字数组合并

"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, nums = [], []
        for log in logs:
            log_list = log.split(' ')
            if log_list[1].isalpha():
                letters.append((log_list[0], ' '.join(log_list[1:])))
            else:
                nums.append(log)
        letters.sort(key=lambda x: (x[1], x[0]))
        return [log[0] + " " + log[1] for log in letters] + nums
