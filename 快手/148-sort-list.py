"""
https://leetcode-cn.com/problems/sort-list/

148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5


Solution
- 用快慢指针方法将数组分成两把
- 对左边和右边分别排序
- 合并拍完序的左右部分

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, fast, slow = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        return self.mergeTwoLists(l, r)

    def mergeTwoLists(self, l1, l2):
        move = head = ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next
