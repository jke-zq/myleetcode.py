class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        A = nums
        while left + 1 < right:
            # while left + 1 < right and A[left] == A[right]:
            #     left += 1
            mid = (left + right) / 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid
        
        return left if A[left] > A[right] else right
                