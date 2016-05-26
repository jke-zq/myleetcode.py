class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return
        start = length - 1
        while start > 0 and nums[start] <= nums[start - 1]:
            start -= 1
        if start == 0:
            nums.reverse()
            
        else:
            j = length - 1
            while j > start - 1:
                if nums[j] > nums[start - 1]:
                    break
                j -= 1
            
            nums[start - 1], nums[j] = nums[j], nums[start - 1]
            nums[start:] = sorted(nums[start:])
            