import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pivot = random.choice(nums)
        # left = []
        # right = []
        # for n in nums:
        #     if n > pivot:
        #         left.append(n)
        #     elif n < pivot:
        #         right.append(n)
        # # print pivot, left, right
        # if k <= len(left):
        #     return self.findKthLargest(left, k)
        # elif k > len(nums) - len(right):
        #     return self.findKthLargest(right, k - (len(nums) - len(right)))
        # return pivot
        
        #second solution
        def partition(left, right, pivot):
            nums[right], nums[pivot] = nums[pivot], nums[right]
            newpivot = left
            # while left < right:
            for i in range(left, right):
                if nums[i] > nums[right]:
                    nums[newpivot], nums[i] = nums[i], nums[newpivot]
                    newpivot += 1
                # left += 1
            nums[right], nums[newpivot] = nums[newpivot], nums[right]
            return newpivot
            
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition(left, right, pivot_idx)
            # print new_pivot_idx, nums
            if new_pivot_idx + 1 < k:
                left = new_pivot_idx + 1
            elif new_pivot_idx + 1 > k:
                right = new_pivot_idx - 1
            else:
                return nums[new_pivot_idx]
            