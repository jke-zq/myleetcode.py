class Solution(object):
    ##tle
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def  maxCoinsRecur(nums):
            if not nums:
                return 1
            else:
                ret = float('-inf')
                key = tuple(nums)
                if key in lookup:
                    return lookup[key]
                for i in range(len(nums)):
                    ret = max(ret, maxCoinsRecur(nums[:i] + nums[i + 1:]) * nums[i])
                lookup[key] = ret
                return ret
        lookup = {}
        
        return maxCoinsRecur(nums)