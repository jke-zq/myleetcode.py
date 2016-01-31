# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, post = dummy, dummy
        for i in range(n):
            post = post.next
        while post.next:
            post, pre = post.next, pre.next
        pre.next = pre.next.next
        return dummy.next