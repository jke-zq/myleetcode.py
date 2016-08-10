class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(x, tag):
            if dp[x]:
                return dp[x]
            ans = x if tag else 0
            for next_x in range(1, x / 2 + 1):
                ans = max(ans, helper(next_x, True) * helper(x - next_x, True))
            dp[x] = ans
            return ans
        dp = [0] * (n + 1)
        return helper(n, False)


# Hint, find the regularity.
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(x):
            if x in (2, 3, 4):
                return x
            return helper(3) * helper(x - 3)
        if n == 2:
            return 1
        if n == 3:
            return 2
        return helper(n)
