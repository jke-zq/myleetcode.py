class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        haved = set()
        # while True:
        #     n = reduce(lambda x, y: x + y ** 2, [int(key) for key in str(n)], 0)
        #     if n in haved:
        #         return False
        #     elif n == 1:
        #         return True
        #     else:
        #         haved.add(n)
        while n != 1:
            n = reduce(lambda x, y: x + y ** 2, [int(k) for k in str(n)], 0)
            if n in haved:
                return False
            else:
                haved.add(n)
        return True