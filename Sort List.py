# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(n1, n2):
            dummy = ListNode(0)
            p = dummy
            while n1 and n2:
                if n1.val < n2.val:
                    p.next, n1, p = n1, n1.next, n1
                else:
                    p.next, n2, p = n2, n2.next, n2
            if n1:
                p.next = n1
            if n2:
                p.next = n2
            return dummy.next
        if not head:
            return None
        if head and not head.next:
            return head
        # dummy = ListNode(0)
        # dummy.next = head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # dummy.next = None
        head2, slow.next = slow.next, None
        h1 = self.sortList(head)
        h2 = self.sortList(head2)
        return merge(h1, h2)
##关键点在于两个Node要拆成1个的