class Solution(object):
	def wiggleSort(self, nums):
		for i in range(1, len(nums)):
			if ((i % 2) and nums[i - 1] > nums[i]) or (
				(not (i % 2) and nums[i - 1] < nums[i])):
			    nums[i - 1], nums[i] = nums[i], nums[i - 1]
			    