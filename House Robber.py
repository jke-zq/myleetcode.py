class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dpi, dpi_1 = max(nums[0], nums[1]), nums[0]
        for i in nums[2:]:
            dpi, dpi_1 = max(i + dpi_1, dpi), dpi
        return dpi