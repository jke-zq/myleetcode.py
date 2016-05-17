class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sets = set(nums)
        ans = 1
        for n in nums:
            if n not in nums:
                continue
            count = 0
            right = n
            while right in sets:
                count += 1
                sets.remove(right)
                right += 1
            left = n - 1
            while left in sets:
                count += 1
                sets.remove(left)
                left -= 1
            ans = max(count, ans)
        return ans
                