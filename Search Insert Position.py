class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (end + start) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return 0
        elif nums[end] < target:
            return len(nums)
        else:
            return start + 1
