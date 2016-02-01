class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def getVal(bitIndex):
        #     return 1 << (33 - bitIndex - 1)
        # index = 1
        # ret = 0
        # while n:
        #     if n & 1:
        #         ret += getVal(index)
        #     n >>= 1
        #     index += 1
        # return ret
        ret = 0
        for i in range(32):
            ret <<= 1
            ret |= n & 1
            n >>= 1
        return ret