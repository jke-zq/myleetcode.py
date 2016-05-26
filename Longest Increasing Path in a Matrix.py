class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(r, c, dp, ans, m, n, matrix, DICTS):
            # if r < 0 or r >= m or c < 0 or c >= n:
            #     return
            if dp[r][c] > 0:
                return dp[r][c]
            count = 1
            for dx, dy in DICTS:
                nr, nc = r + dx, c + dy
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if matrix[r][c] > matrix[nr][nc]:
                    count = max(count, 1 + dfs(nr, nc, dp, ans, m, n, matrix, DICTS))
            dp[r][c] = count
            ans[0] = max(ans[0], dp[r][c])
            return dp[r][c]
            
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for __ in range(m)]
        ans = [0]
        DICTS = ((1, 0), (-1, 0), (0, -1), (0, 1))
        for i in range(m):
            for j in range(n):
                dfs(i, j, dp, ans, m, n, matrix, DICTS)
        return ans[0]