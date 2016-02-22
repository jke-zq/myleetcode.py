import operator
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        index, __ = max(enumerate(height), key = operator.itemgetter(1))
        ret = 0
        tallest = 0
        for i in range(index):
            if tallest > height[i]:
                ret += tallest - height[i]
            else:
                tallest = height[i]
        tallest = 0
        for i in range(len(height) - 1, index, -1):
            if tallest > height[i]:
                ret += tallest - height[i]
            else:
                tallest = height[i]
        return ret
        