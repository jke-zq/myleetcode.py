class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        setv = set(nums)
        
        ans = 0
        for n in nums:
            if n in setv:
                count = 1
                setv.remove(n)
                left = n - 1
                while left in setv:
                    count += 1
                    setv.remove(left)
                    left -= 1
                    
                right = n + 1
                while right in setv:
                    count += 1
                    setv.remove(right)
                    right += 1
                    
                ans = max(ans, count)
        return ans
                
        