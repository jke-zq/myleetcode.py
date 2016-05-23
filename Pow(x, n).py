class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -1 * n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            ans = self.myPow(x, n / 2)
            return ans * ans