class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1]
        for i in range(1, len(nums)):
            ret.append(ret[i - 1] * nums[i - 1])
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= count
            count *= nums[i]
        return ret
            
            
            