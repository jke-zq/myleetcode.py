# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, even = head, head.next
        left, right = odd, even
        node = head.next.next
        # while node:
        #     left.next, left = node, node
        #     node = node.next
        #     right.next, right = node, node
        #     if node:
        #         node = node.next
        while right and right.next:
            left.next = right.next
            left = right.next
            right.next = left.next
            right = left.next
        left.next = even
        return odd
        