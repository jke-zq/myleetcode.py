# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        n1, n2 = headA, headB
        while n1 and n1.next:
            n1 = n1.next
        while n2 and n2.next:
            n2 = n2.next
        if n2 != n1:
            return None
        n1, n2 = headA, headB
        while n1 and n2:
            n1, n2 = n1.next, n2.next
        newn1 = headA if n1 else headB
        newn2 = headB if n1 else headA
        oldn = n1 if n1 else n2
        while oldn:
            newn1, oldn = newn1.next, oldn.next
        while newn1 != newn2:
            newn1, newn2 = newn1.next, newn2.next
        return newn1
        ##solution b
        ##loop headA, then loop headB, the same distance.
        