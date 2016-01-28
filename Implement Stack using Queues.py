class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        top = self.pop()
        self.push(top)
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue == []
        