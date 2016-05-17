# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        groups = length / k
        dummy = ListNode(0)
        cur = dummy
        for __ in range(groups):
            tail = head
            for __ in range(k):
                tmp = head.next
                head.next, cur.next = cur.next, head
                head = tmp
            cur = tail
        cur.next = head
        return dummy.next