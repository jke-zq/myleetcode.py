class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse = 0
        n = x
        while n:
            reverse *= 10
            reverse += n % 10
            n /= 10
        return x == reverse