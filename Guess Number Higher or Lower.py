# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        start, end = 0, n + 1
        while start + 1 < end:
            mid = (end + start) / 2
            tag = guess(mid)
            if tag == 0:
                return mid
            elif tag == 1:
                start = mid
            else:
                end = mid

