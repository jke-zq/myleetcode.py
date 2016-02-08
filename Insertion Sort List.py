# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def isSorted(head):
            while head and head.next:
                if head.val > head.next.val:
                    return False
                head = head.next
            return True
        if not head or isSorted(head):
            return head
        dummy = ListNode(-1)
        p = head
        while p:
            q = dummy
            while q.next and q.next.val < p.val:
                q = q.next
            # tmp = p.next
            # p.next = q.next
            # q.next = p
            # p = tmp
            q.next, p.next, p = p, q.next, p.next
        return dummy.next
            
                
        
##关于list的问题：
####我感觉还是把list单独区分开比较好。比如上面的代码是dummy的list是排好序的，headlist是待排序和遍历的;
####这笔把这俩list放在一起，用tail_node做区分来的清晰。