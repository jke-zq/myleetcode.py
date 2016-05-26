# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        self.ans = self.help(nestedList)
        self.length = len(self.ans)
        
    def help(self, nestedList):
        ans = []
        for nint in nestedList:
            if nint.isInteger():
                ans.append(nint.getInteger())
            else:
                ans.extend(self.help(nint.getList()))
        return ans
        
    def next(self):
        """
        :rtype: int
        """
        val = self.ans[self.index]
        self.index += 1
        return val
                
                
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.length
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




## solution two

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.store = [[nestedList, 0]]
        

    def next(self):
        """
        :rtype: int
        """
        # val = self.store[-1][0][self.store[-1][1]]
        # self.store[-1][1] += 1
        # return val
        nestedList, i = self.store[-1]
        self.store[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.store:
            nested, i = self.store[-1]
            if i == len(nested):
                self.store.pop()
            elif nested[i].isInteger():
                return True
            else:
                self.store[-1][1] += 1
                self.store.append([nested[i].getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
