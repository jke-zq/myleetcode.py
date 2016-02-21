class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def doCombine(pos, left, nums, tmp, ret):
            if left == 0:
                ret.append(tmp[::])
            else:
                for i in range(pos, len(nums) - left + 1):
                    tmp.append(nums[i])
                    doCombine(i + 1, left - 1, nums, tmp, ret)
                    tmp.pop()
        nums = range(1, n + 1)
        tmp, ret = [], []
        doCombine(0, k, nums, tmp, ret)
        return ret