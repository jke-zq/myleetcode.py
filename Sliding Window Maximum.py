import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = collections.deque()
        ans = []
        if not nums:
            return ans
        length = len(nums)
        for i in range(length):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
            if queue[0] == i - k + 1:
                queue.popleft()
        return ans
        