class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findLine(nums):
            if not nums:
                return 0
            dpi, dpi_1 = 0, 0
            for n in nums:
                dpi, dpi_1 = max(dpi_1 + n, dpi), dpi
            return dpi
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(findLine(nums[1:]), findLine(nums[:-1]))