# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float("inf"))
        dummy.next = head
        p = dummy
        while p.next:
            node = p.next
            if node.val == val:
                p.next = node.next
            else:
                p = node
        return dummy.next