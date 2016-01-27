# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return None
        # pre, right = head, head.next
        # while right:
        #     if right.val == pre.val:
        #         tmp = right.next
        #         right.next = None
        #         right = tmp
        #     else:
        #         pre.next, pre, right = right, right, right.next
        # pre.next = None
        # return head
        cur = head
        while cur and cur.next:
            next = cur.next
            if next.val == cur.val:
                cur.next = next.next
            else:
                cur = next
        return head
            