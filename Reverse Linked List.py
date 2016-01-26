# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy = ListNode(float("inf"))
        # cur = head
        # while cur:
        #     dummy.next, cur.next, cur = cur, dummy.next, cur.next
        # return dummy.next
        def doRecur(node, head):
            if not node:
                return head
            tmp, node.next = node.next, head
            return doRecur(tmp, node)
        return doRecur(head, None)
            
            
            