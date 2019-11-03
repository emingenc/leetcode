"""
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_head = ListNode(None)
        l_current = ListNode(None)

        l_head = l_current

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l_current.next = l1
                l1 = l1.next
            else:
                l_current.next = l2
                l2 = l2.next
            l_current = l_current.next

        if l1 is not None:
            l_current.next = l1

        if l2 is not None:
            l_current.next = l2

        return l_head.next
