class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = -1, x + 1
        while start + 1 < end:
            mid = (end + start) / 2
            ret = mid ** 2
            if ret == x:
                return mid
            elif ret > x:
                end = mid
            else:
                start = mid
        return start

