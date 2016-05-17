class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, length, visited, tmp, ans, nums):
            if start == length:
                ans.append(tmp[:])
                return
            for i in range(length):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                ## error
                if visited[i]:
                    continue
                tmp.append(nums[i])
                visited[i] = True
                dfs(start + 1, length, visited, tmp, ans, nums)
                visited[i] = False
                tmp.pop()
                
        if not nums:
            return []
        
        nums = sorted(nums)
        length = len(nums)
        tmp, ans = [], []
        visited = [False] * length
        dfs(0, length, visited, tmp, ans, nums)
        return ans
        