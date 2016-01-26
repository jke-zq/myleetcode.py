# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if (not head) or (not head.next):
            return
        fast, slow, pre = head, head, None
        while fast and fast.next:
            slow, fast, pre = slow.next, fast.next.next, slow
            # slow = slow.next
            # fast = fast.next.next
        tail, right, pre.next = None, slow, None
        # tail = slow.next
        # # if not tail:
        # #     return
        # slow.next = None
        # right = tail.next
        # tail.next = None
        while right:
            right.next, tail, right = tail, right, right.next
            # tmp = right.next
            # right.next = tail
            # tail = right
            # right = tmp
        dummy = ListNode(float("inf"))
        p = dummy
        while head and tail:
            p.next, p, head = head, head, head.next
            p.next, p, tail = tail, tail, tail.next
        head = dummy.next
        # if not head:
        #     return
        # fast, slow = head, head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # tail = slow.next
        # if not tail:
        #     return
        # slow.next = None
        # right = tail.next
        # tail.next = None
        # while right:
        #     tmp = right.next
        #     right.next = tail
        #     tail = right
        #     right = tmp
        # ret = head
        # p = head
        # head = head.next
        # while head or tail:
        #     p.next = tail
        #     tail = tail.next
        #     p.next.next = head
        #     p = head
        #     if head:
        #         head = head.next
        # head = ret
            
        