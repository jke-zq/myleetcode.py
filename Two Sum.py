class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}
        for index, val in enumerate(nums):
            pairs[val] = index
        for index, val in enumerate(nums):
            left = target - val
            if left in pairs:
                if index != pairs[left]:
                    return sorted([pairs[left] + 1, index + 1])
        