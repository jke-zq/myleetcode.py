# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        # self.head = head
        # self.cur = head
        # self.init(5)
        ##
        # self.head = head
        # self.cur = self.head.next
        # self.index = 1
        # self.ans = self.head
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        # """
        # if self.index < self.length:
        #     ans = self.vals[self.index]
        #     self.index += 1
        #     if self.index == self.length:
        #         self.init(5)
        #     return ans
        # return None
        ##
        # if not self.cur:
        #     return self.ans.val
        # if random.random() < 1.0 / self.index:
        #     self.ans = self.cur
        # self.cur = self.cur.next
        # self.index += 1
        # if not self.cur:
        #     self.cur = self.head.next
        #     self.index = 1
        #     self.ans = self.head
        ### TLE
        # if self.head is None:
        #     return
        # # Use a different seed value so that we don't get
        # # same result each time we run this program
        # # remove this, TLE to WA
        # # random.seed()
        # result = self.head.val
        # current = self.head
        # n = 2
        # while(current is not None):
        #     if (random.randrange(n) == 0 ):
        #         result = current.val
        #     current = current.next
        #     n += 1
        # return result
        if not self.head:
            return None
        ans = None
        cur = self.head
        n = 0
        while cur:
            if random.randint(0, n) == 0:
                ans = cur.val
            cur = cur.next
            n += 1
        return ans

        # return self.ans.val


    # def init(self, length):
    #     self.index = 0
    #     self.length = 0
    #     self.vals = []
    #     # if not self.cur:
    #     #     self.cur = self.head
    #     for i in range(length):
    #         if not self.cur:
    #             self.cur = self.head
    #         self.vals.append(self.cur.val)
    #         self.cur = self.cur.next
    #         self.length += 1
    #     random.shuffle(self.vals)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
