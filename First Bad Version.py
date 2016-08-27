# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n + 1
        while start  + 1 < end:
            mid = (end + start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        return end
