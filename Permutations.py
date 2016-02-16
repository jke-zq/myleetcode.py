class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(left, visited, nums, tmp, ret):
            if not left:
                ret.append(tmp[::])
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        tmp.append(nums[i])
                        visited[i] = True
                        dfs(left - 1, visited, nums, tmp, ret)
                        visited[i] = False
                        tmp.pop()
                        
        
        nums.sort()
        length = len(nums)
        ret, tmp = [], []
        visited = [False] * length
        dfs(length, visited, nums, tmp, ret)
        return ret