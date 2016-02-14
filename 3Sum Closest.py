class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = 0
        distance = float('inf')
        nums = sorted(nums)
        size = len(nums)
        for i in range(size):
            left = i + 1
            right = size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < distance:
                    distance = abs(total - target)
                    ret = total
                if total > target:
                    right -= 1
                else:
                    left += 1
                    
        return ret