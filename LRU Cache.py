class LRUCache(object):
    class ListNode(object):
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.head = LRUCache.ListNode(0, 0)
        self.tail = self.head
        self.dicts = {}
    
    def __push_back__(self, node):
        self.dicts[node.key] = self.tail
        self.tail.next = node
        self.tail = node
        
    def __pop_front__(self):
        if self.head == self.tail:
            return
        deleteOne, frontOne = self.head.next, self.head.next.next
        self.dicts.pop(deleteOne.key)
        self.head.next = frontOne
        if frontOne:
            self.dicts[frontOne.key] = self.head
        else:
            self.tail = self.head ## if delete the self.tail
            
    def __touch__(self, pre):
        if pre.next == self.tail:
            return
        node, nextOne = pre.next, pre.next.next
        pre.next = nextOne
        self.dicts[nextOne.key] = pre
        self.dicts.pop(node.key)
        self.__push_back__(node)
        # self.tail.next = node
        # self.dicts[node.key] = self.tail
        # self.tail = node

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dicts:
            return -1
        pre = self.dicts[key]
        ans = pre.next.val
        self.__touch__(pre)
        return ans

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dicts:
            pre = self.dicts[key]
            pre.next.val = value
            self.__touch__(pre)
            return
        node = LRUCache.ListNode(key, value)
        self.count += 1
        self.__push_back__(node)
        if self.count > self.capacity:
            self.__pop_front__()
            