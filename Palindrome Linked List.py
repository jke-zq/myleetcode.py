# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #other solution: reverse the first half of the linked list
        
        if (not head) or (not head.next):
            return True
        fast, slow, pre = head, head, None
        while fast and fast.next:
            fast, slow, pre = fast.next.next, slow.next, slow
        tail, right, pre.next = None, slow, None
        while right:
            right.next, right, tail = tail, right.next, right
        l1, l2 = head, tail
        while l1 and l2:
            if l1.val != l2.val:
                return False
            else:
                l1, l2 = l1.next, l2.next
        return True;
                
        