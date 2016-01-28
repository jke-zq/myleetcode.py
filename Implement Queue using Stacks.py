class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.outstack = []
        self.instack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outstack:
            self.outstack, self.instack = self.instack[::-1], []
        return self.outstack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.outstack and not self.instack
        