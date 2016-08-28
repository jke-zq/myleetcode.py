class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        while b:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            a, b = a ^ b, (a & b) << 1
        return a

