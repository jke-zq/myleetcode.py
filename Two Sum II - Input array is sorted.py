class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def helper(nums, start, end, target):
            start, end = start - 1, end + 1
            while start + 1 < end:
                mid = (start + end) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid
                else:
                    start = mid
            return None
        length = len(numbers)
        for i in range(length):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            other = helper(numbers, i + 1, length - 1, target - numbers[i])
            if other:
                return (i + 1, other + 1)
        return None
