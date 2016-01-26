class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tag = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if tag == nums[i]:
                count += 1
            else:
                count -= 1
                if not count:
                    count = 1
                    tag = nums[i]
        return tag