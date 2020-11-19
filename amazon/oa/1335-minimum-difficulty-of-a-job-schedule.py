"""
1335. Minimum Difficulty of a Job Schedule

https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule/

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1

Input: jobDifficulty = [6,5,4,3,2,1], d = 2

Output: 7

Explanation: First day you can finish the first 5 jobs, total difficulty = 6. Second day you can finish the last job, total difficulty = 1.

The difficulty of the schedule = 6 + 1 = 7

Example 2:

Input: jobDifficulty = [9,9,9], d = 4

Output: -1

Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3

Output: 3

Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3

Output: 15

Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6

Output: 843

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10

"""

# Recursion with Memoization, Top-down

# Starting from the last day, we simply try out all the possible schdules for each day.
# We track the intended finished day (intended) and the first i-th jobs (end).

"""
The idea is to to finish up till i'th job in d - k days and finish rest of the jobs in k days.

f(i,k) = min( f(j,k) + max_job_difficulty_for_i_th_day) for i <= j <= n - k + 1
where max_job_difficulty_for_i_th_day is nothing but max( jobDifficulty[i:j] )

Base condition: When we have only 1 day left then we have to finish the rest of the unfinished jobs, i.e. value for that day is max( jobDifficulty[i:] )
"""

"""
Difficulty of each day is max difficulty of a job done in that day

Given array of job difficulty and integer d, return minimum difficulty of a job schedule

Ideas:
- 2 components, depth (days) + how many jobs we choose (len(jobdifficulty))
- for a given day can we choose x remaining jobs
- how do we keep track ofremaining jobs, have a pointer and jobs remaining
"""




from functools import lru_cache
from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        arr = jobDifficulty

        @lru_cache(None)
        def helper(st, k):
            # only one day left so we have to finish rest of the unfinished jobs
            if k == 1:
                return max(arr[st:])

            # cur_max is max from i to j'th index, which is value on k'th day
            cur_max, ret = 0, float('inf')
            for i in range(st, len(arr)-k+1):
                cur_max = max(cur_max, arr[i])
                ret = min(ret, cur_max + helper(i+1, k - 1))
            return ret

        return helper(0, d)
