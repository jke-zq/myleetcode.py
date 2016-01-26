class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # size = len(nums)
        # start, pre = 0, 0
        # for i in range(size):
        #     if nums[i] != 0:
        #         nums[start], nums[pre] = nums[pre], nums[start]
        #         start += 1
        #         pre += 1
        #     else:
        #         pre += 1
        
        y = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[y], nums[i] = nums[i], nums[y]
                y += 1