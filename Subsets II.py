class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, end, nums, tmp, ret):
            ret.append(tmp[::])
            for i in range(start, end):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    tmp.append(nums[i])
                    dfs(i + 1, end, nums, tmp, ret)
                    tmp.pop()
                    
        nums.sort()
        length = len(nums)
        ret, tmp = [], []
        dfs(0, length, nums, tmp, ret)
        return ret