class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(start, end, dp, nums):
            if start + 1 >= end:
                return 0
            if dp[start][end] > 0:
                return dp[start][end]
            ans = 0
            for i in range(start + 1, end):
                ans = max(ans, dfs(start, i, dp, nums) + dfs(i, end, dp, nums) + nums[start] * nums[end] * nums[i])
            dp[start][end] = ans
            return dp[start][end]
                
        nums.append(1)
        nums.insert(0, 1)
        length = len(nums)
        dp = [[0] * length for __ in range(length)]
        dfs(0, length - 1, dp, nums)
        return dp[0][length - 1]