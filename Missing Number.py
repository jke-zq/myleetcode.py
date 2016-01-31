class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # total = (1 + n) * n / 2
        # ret = total - sum(nums)
        # if ret:
        #     return ret
        # else:
        #     if 0 in nums:
        #         return n + 1
        #     else:
        #         return 0
        
        ##xor
        return reduce(operator.xor, nums, reduce(operator.xor, range(len(nums) + 1)))