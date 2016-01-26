class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        y = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[y], nums[i] = nums[i], nums[y]
                y += 1
        nums = nums[:y]
        return y