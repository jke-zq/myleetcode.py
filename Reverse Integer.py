class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        ret = 0
        while x:
            if ret > MAX_INT / 10 or ret * 10 > MAX_INT - x % 10:
                return 0
            ret *= 10
            ret += x % 10
            x /= 10
        return sign * ret