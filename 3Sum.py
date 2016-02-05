class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = set()
        onums = sorted(nums)
        i = 0
        while i < len(nums):
            if i > 0 and onums[i] == onums[i - 1]:
                i += 1
                continue
            need = 0 - onums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if onums[left] + onums[right] < need:
                    left += 1
                elif onums[left] + onums[right] > need:
                    right -= 1
                else:
                    ret.add((onums[i], onums[left], onums[right]))
                    left += 1
                    right -= 1
            i += 1
        return [list(k) for k in ret]
            