# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        cur = head
        hashPairs = {}
        while cur:
            hashPairs[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                hashPairs[cur].next = hashPairs[cur.next]
            if cur.random:
                hashPairs[cur].random = hashPairs[cur.random]
            cur = cur.next
        return hashPairs[head]