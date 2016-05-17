class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## check if digit?
        if not s:
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        for i in range(1, length + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i > 1:
                intV = int(s[i - 2:i])
                if 10 <= intV <= 26:
                    dp[i] += dp[i - 2]
        return dp[-1]
        