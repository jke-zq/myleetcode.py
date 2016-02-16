class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(left, visited, tmp, ret, nums):
            if not left:
                ret.append(tmp[::])
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                            continue
                        else:
                            visited[i] = True
                            tmp.append(nums[i])
                            dfs(left - 1, visited, tmp, ret, nums)
                            tmp.pop()
                            visited[i] = False
                            
        nums.sort()
        length, tmp, ret = len(nums), [], []
        visited = [False] * length
        dfs(length, visited, tmp, ret, nums)
        return ret