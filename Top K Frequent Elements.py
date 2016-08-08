import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if k == len(nums):
        #     return list(set(nums))
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        ans = sorted(count.keys(), key=lambda x:count[x], reverse=True)
        return ans[0:k]


