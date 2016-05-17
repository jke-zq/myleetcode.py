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
        # Definition for singly-linked list.

#solution B
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ##solution b
        ##loop headA, then loop headB, the same distance.
        p1, p2 = headA, headB
        taila, tailb = False, False
        while p1 and p2:
            if p1 == p2:
                return p1
            if not p1.next and not taila:
                p1 = headB
                taila = True
            else:
                p1 = p1.next
            if not p2.next and not tailb:
                p2 = headA
                tailb = True
            else:
                p2 = p2.next
        return None

#solution c:
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
        if headA is None or headB is None:
            return None
        
        endA, endB = False, False
        pA, pB = headA, headB
        while pA and pB:
            if pA == pB:
                return pA
            if pA.next:
                pA = pA.next
            elif not endA:
                pA = headB
                endA = True
            else:
                return None
                
            if pB.next:
                pB = pB.next
            elif not endB:
                pB = headA
                endB = True
            else:
                return None
        return None
        