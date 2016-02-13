class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max = float('-inf'), 0
        for n in nums:
            local_max = max(n, local_max + n)
            global_max = max(global_max, local_max)
        return global_max