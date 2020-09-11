"""
https://leetcode.com/problems/frog-jump/


403. Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit there may 
or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.


dp一维数组每个元素记录key:石块位置 val:到达这个位置需要的步数
通过遍历每个石块位置所需要的步数，判断下一步能到达的位置
最后看最后石块位置的步数是不是大于1

使用bfs，queue里每个节点包含石头位置和到达石头的步数
注意queue起始元素是(0, 0)

"""

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {stones[i]: set() for i in range(n)}
        dp[0].add(0)
        for i in range(n):
            for k in dp[stones[i]]:
                for step in range(k - 1, k + 2, 1):
                    if step > 0 and stones[i] + step in dp:
                        dp[stones[i] + step].add(step)
        return len(dp[stones[-1]]) > 0


class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        for i in range(3, len(stones)):
            if stones[i] > stones[i-1] * 2:
                return False
        last_pos = stones[-1]
        queue = [(0, 0)]
        set_pos = set(stones)
        while queue:
            pos, k = queue.pop(0)
            if pos == last_pos:
                return True
            for step in [k-1, k, k + 1]:
                if step <= 0:
                    continue
                next_pos = pos + step
                if next_pos in set_pos:
                    queue.append((next_pos, step))
        return False
