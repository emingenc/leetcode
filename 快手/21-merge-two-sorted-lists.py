"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = l = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                tmp = ListNode(l2.val)
                l2 = l2.next
                l.next = tmp
            else:
                tmp = ListNode(l1.val)
                l1 = l1.next
                l.next = tmp
            l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
        return dummy.next
