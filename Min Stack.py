class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.mins:
            self.mins.append(x)
        elif self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        x = self.stack.pop()
        if self.mins[-1] == x:
            self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
        

##soulution B
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: nothing
        """
        x = self.stack.pop()
        if x < 0:
            self.min -= x

    def top(self):
        """
        :rtype: int
        """
        x = self.stack[-1]
        if x < 0:
            return self.min
        else:
            return self.min + x

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        