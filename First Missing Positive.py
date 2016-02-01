class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        i = 0
        while i < size:
            # if i + 1 != nums[i] and 0 < nums[i] <= size and nums[nums[i] - 1] != nums[i]:
            if 0 < nums[i] <= size and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
            
        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        return len(nums) + 1