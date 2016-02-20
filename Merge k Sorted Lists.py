# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ##heap
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            smallest = heapq.heappop(heap)[1]
            cur.next, cur = smallest, smallest
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next
        ##TLE
        # def merge(left, right):
        #     if left >= right:
        #         return
        #     mid = (left + right) / 2
        #     merge(left, mid)
        #     merge(mid + 1, right)
        #     if mid + 1 > right or lists[mid].val <= lists[mid + 1].val:
        #         return
        #     ##merge
        #     tmp = []
        #     j = mid + 1
        #     for i in range(left, mid + 1):
        #         while j <= right and lists[i].val > lists[j].val:
        #             tmp.append(lists[j])
        #             j += 1
        #         tmp.append(lists[i])
        #     lists[left:left + len(tmp)] = tmp
        # start = 0
        # ret = ListNode(-1)
        # dummy = ret
        # lists = filter(lambda i:i != None, lists)
        # n = len(lists)
        # while len(lists):
        #     merge(0, n - 1)
        #     for i in range(0, n):
        #         if lists[i]:
        #             ret.next = lists[i]
        #             ret = ret.next
        #             lists[i] = lists[i].next
        #             if not lists[i]:
        #                 lists.pop(i)
        #                 n -= 1
        #             break
        # return dummy.next
                
        