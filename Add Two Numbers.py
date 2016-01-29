# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        cherry = 0
        while l1 and l2:
            p.next = ListNode(0)
            p = p.next
            p.val = cherry + l1.val + l2.val
            p.val, cherry = p.val % 10, p.val / 10
            l1, l2 = l1.next, l2.next
        
        left = l1 if l1 else l2
        while left:
            p.next = ListNode(0)
            p = p.next
            p.val = cherry + left.val
            p.val, cherry = p.val % 10, p.val / 10
            left = left.next
        if cherry:
            p.next = ListNode(cherry)
        return dummy.next