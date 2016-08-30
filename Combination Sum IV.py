class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # TLE
        # def helper(nums, left, ans):
        #     if left == 0:
        #         ans[0] += 1
        #         return
        #     for n in nums:
        #         if n > left:
        #             return
        #         helper(nums, left - n, ans)

        # nums.sort()
        # ans = [0]
        # helper(nums, target, ans)
        # return ans[0]

        ## TLE [3,33,333] 1000
        def ms(left, nums, dp):
            if dp[left] > 0:
                return dp[left]
            ans = 0
            for n in nums:
                if left > n:
                    ans += ms(left - n, nums, dp)
                elif left == n:
                    ans += 1
                else:
                    break
            dp[left] = ans
            return dp[left]
        nums.sort()
        dp = [0] * (target + 1)
        ms(target, nums, dp)
        return dp[target]


