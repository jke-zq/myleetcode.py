class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if len(nums) < 2:
        #     return False
        # if len(nums) <= k:
        #     return len(set(nums)) < len(nums)
        # values = set(nums[:k + 1])
        # for i in range(k + 1, len(nums)):
        #     if len(values) != k + 1:
        #         return True
        #     else:
        #         values.remove(nums[i - k - 1])
        #         values.add(nums[i])
        # return len(values) != k + 1                
                
        lookup = {}
        for i, n in enumerate(nums):
            if n in lookup:
                if i - lookup[n] <= k:
                    return True
                else:
                    lookup[n] = i
            else:
                lookup[n] = i
        return False