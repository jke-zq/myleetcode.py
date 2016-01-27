class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 2:
        #     return n
        # else:
        #     return self.climbStairs(n - 2) + self.climbStairs(n - 1)
        # if n <= 2:
        #     return n
        # a, b = 1, 2
        # n -= 2
        # while n:
        #     a, b = b, b + a
        #     n -= 1
        # return b
        a, b = 0, 1
        while n:
            a, b = b, a + b
            n -= 1
        return b