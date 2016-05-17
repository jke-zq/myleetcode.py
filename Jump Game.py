class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        # length = len(nums)
        # dp = [False] * length
        # dp[0] = True
        # for i in range(length):
        #     for j in range(i - 1, -1, -1):
        #         if dp[j] and i - j <= nums[j]:
        #             dp[i] = True
        #             break
        # return dp[-1]
        
        maxIndex = 0
        length = len(nums)
        for i in range(0, length):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + nums[i])
            if maxIndex >= length - 1:
                return True
        