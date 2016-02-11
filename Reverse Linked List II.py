# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        tail = pre.next
        for i in range(n - m):
            ##work
            # pre.next, tail.next.next, tail.next = tail.next, pre.next, tail.next.next
            ##not work
            print tail.next, tail.next.next, pre.next
            tmp = tail.next
            tail.next, tmp.next, pre.next = tail.next.next, pre.next, tail.next
            # print tail.next, tail.next.next, pre.next
            # tail.next.next, pre.next, tail.next = pre.next, tail.next, tail.next.next
            # tmp = tail.next
            # tail.next, pre.next, tmp.next = tmp.next, tmp, pre.next
            
        return dummy.next
##import
##multi variables assigment:
#ie: tail.next, tail.next.next = a, b. 
#when assigning the b to tail.next.next, the value of tail.next.next equals to a.next.
#Because the tail.next hase assinged to a.
            