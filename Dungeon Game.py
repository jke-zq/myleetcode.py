class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        ## wrong answer
        # m, n = len(dungeon), len(dungeon[0])
        # dp = [[float('-inf')] * n for __ in range(m)]
        # dp[0][0] = dungeon[0][0] if dungeon[0][0] < 0 else 0
        # lefts = [[0] * n for __ in range(m)]
        # lefts[0][0] = dungeon[0][0]
        
        # for i in range(1, n):
        #     dp[0][i] = dp[0][i - 1]
        #     if dungeon[0][i] < 0:
        #         dp[0][i] += min(0, lefts[0][i - 1] - dp[0][i - 1] + dungeon[0][i])
        #     lefts[0][i] = lefts[0][i - 1] + dungeon[0][i]
        #     # print 0, i, dp[0][i]
        
        # for i in range(1, m):
        #     dp[i][0] = dp[i - 1][0]
        #     if dungeon[i][0] < 0:
        #         dp[i][0] += min(0, lefts[i - 1][0] - dp[i - 1][0] + dungeon[i][0])
        #     lefts[i][0] = lefts[i - 1][0] + dungeon[i][0]
        #     # print i, 0, dp[i][0]
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         up = dp[i][j - 1]
        #         left = dp[i - 1][j]
        #         if dungeon[i][j] < 0:
        #             up += min(0, lefts[i][j - 1] - up + dungeon[i][j])
        #             left += min(0, lefts[i - 1][j] - left + dungeon[i][j])
        #         if up < left or (up == left and lefts[i - 1][j] >= lefts[i][j - 1]):
        #             dp[i][j] = left
        #             lefts[i][j] = lefts[i - 1][j] + dungeon[i][j]
        #         if up > left or (up == left and lefts[i - 1][j] < lefts[i][j - 1]):
        #             dp[i][j] = up
        #             lefts[i][j] = lefts[i][j - 1] + dungeon[i][j]
                    
        #         # print i, j, dp[i][j], lefts[i][j]
        # ret = dp[m - 1][n - 1]
        # if ret <= 0:
        #     return ret * -1 + 1
        # else:
        #     return 0
        
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for __ in range(m)]
        
        dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                right = max(dp[i][j + 1] - dungeon[i][j], 1)
                down = max(dp[i + 1][j] - dungeon[i][j], 1)
                dp[i][j] = min(down, right)
        return dp[0][0]