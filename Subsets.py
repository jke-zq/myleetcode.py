class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, end, tmp, nums, ret):
            ret.append(tmp[::])
            for i in range(start, end):
                tmp.append(nums[i])
                dfs(i + 1, end, tmp, nums, ret)
                tmp.pop()
                
        nums.sort()
        length = len(nums)
        ret = []
        tmp = []
        dfs(0, length, tmp, nums, ret)
        return ret