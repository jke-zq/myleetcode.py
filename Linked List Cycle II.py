# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = head.next
        slow = head
        while slow != fast:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next

        # take one step
        slow = slow.next
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
