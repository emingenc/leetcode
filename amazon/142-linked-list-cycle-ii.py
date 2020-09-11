
"""
https://leetcode.com/problems/linked-list-cycle-ii/description/

142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position 
(0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 
Follow-up:
Can you solve it without using extra space?

Solution

起点到入口点距离是a, 入口点到环内相遇点距离 x, 环的距离为c
快指针走了 a + x + c
慢指针走了 a + x
2(a + x) = a + x + c
c = a + x
a = c - x
第一次相遇后将快指针设置为头指针快慢指针第二次相遇(直走一步)为入口点

"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
