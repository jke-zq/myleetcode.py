class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max, local_min = float('-inf'), 1, 1
        for n in nums:
            local_max, local_min = max(n, local_max * n, local_min * n), min(n, local_max * n, local_min * n)
            global_max = max(global_max, local_max)
        return global_max
            