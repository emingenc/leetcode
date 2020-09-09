"""
https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists


Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

用递归方法
"""


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            ans = ListNode(l2.val, self.mergeTwoLists(l1, l2.next))
        else:
            ans = ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
        return ans
