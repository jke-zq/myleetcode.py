class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        left, right = 0, size - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
                ##because of there is not '2 between left and i.
                # if i == left - 1:
                #     i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        
            

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return None
        
        left, right = 0, len(nums) - 1
        pre = 0
        while left <= right:
            if nums[left] == 0:
                nums[pre], nums[left] = nums[left], nums[pre]
                pre += 1
                left += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        