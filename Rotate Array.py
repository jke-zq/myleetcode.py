class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        k = k % (right + 1)
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

##loop in a circle
# class Solution2:
#     # @param nums, a list of integer
#     # @param k, num of steps
#     # @return nothing, please modify the nums list in-place.
#     def rotate(self, nums, k):
#         k %= len(nums)
#         num_cycles = gcd(len(nums), k)
#         cycle_len = len(nums) / num_cycles
#         for i in xrange(num_cycles):
#             self.apply_cycle_permutation(k, i, cycle_len, nums)
    
#     def apply_cycle_permutation(self, k, offset, cycle_len, nums):
#         tmp = nums[offset]
#         for i in xrange(1, cycle_len):
#             nums[(offset+i*k) % len(nums)], tmp = tmp, nums[(offset+i*k) % len(nums)]
#         nums[offset] = tmp
#          