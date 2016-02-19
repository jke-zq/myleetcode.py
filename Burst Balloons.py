class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #tle
        # def  maxCoinsRecur(nums):
        #     if not nums:
        #         return 0
        #     else:
        #         ret = float('-inf')
        #         key = tuple(nums)
        #         if key in lookup:
        #             return lookup[key]
        #         for i in range(len(nums)):
        #             left = 1 if i < 1 else nums[i - 1]
        #             right = 1 if i == len(nums) - 1 else nums[i + 1]
        #             ##wrong
        #             # ret = max(ret, maxCoinsRecur(nums[:i]) + left * right * nums[i] + maxCoinsRecur(nums[i + 1:]))
        #             ret = max(ret, maxCoinsRecur(nums[:i] + nums[i + 1:]) + left * right * nums[i])
        #         lookup[key] = ret
        #         return ret
        # lookup = {}
        
        # return maxCoinsRecur(nums)
if __name__ == '__main__':
    nums = [42,23,62,2,89,97,26,82,47,23,9,2,9,11,53,49,40,3,88,76,63,11,79,37,52,91,5,44,71,69,20,5,74,41,70,68,26,16,62,53,47,46,26,27,99,72,4,40,77,74,89,19,26,7,30,79,49,75,51,28,47,26,55,81,82,15,21,89,51,10,0,50,31,32,38,7,99,13,23,98,68,9,54,15,34,52,58,48,66,75,6,15,91,33,15,37,25,98,98,77,60,16,82,89,48,43,1,85,39,99,95,86,45,90,73,45,93,99,39,57,32,47,35,79,25,54,98,34,60,90,38,40,5,5,96,21,18,93,69,38,85,49,15,77,84,70,52,87,73,15,65]
    # print Solution().maxCoins(nums)
    print len(nums)
# https://leetcode.com/discuss/72216/share-some-analysis-and-explanations
##Be Naive First
# Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted. This indicate that we can use memorization (top down) or dynamic programming (bottom up) for all the cases from small numbers of balloon until n balloons. How many cases are there? For k balloons there are C(n, k) cases and for each case it need to scan the k balloons to compare. The sum is quite big still. It is better than O(n!) but worse than O(2^n).
##Better idea
# We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems from the previous analysis.
# Well, the nature way to divide the problem is burst one balloon and separate the balloons into 2 sub sections one on the left and one one the right. However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.
# Then another interesting idea come up. Which is quite often seen in dp problem analysis. That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.
# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!
# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].
# OK. Think about n balloons if i is the last one to burst, what now?
# We can see that the balloons is again separated into 2 sections. But this time since the balloon i is the last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other! Therefore we can do either recursive method with memoization or dp.
# Final
# Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries and also burst all the zero balloons in the first round since they won't give any coins. The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##DC
        # def  maxCoinsRecur(left, right):
        #     if left == right:
        #         return 0
        #     else:
        #         if lookup[left][right] == 0:
        #             for i in range(left + 1, right):
        #                 lookup[left][right] = max(lookup[left][right], maxCoinsRecur(left, i) + maxCoinsRecur(i, right) + nums[left] * nums[i] * nums[right])
        #         return lookup[left][right]
                    
        # nums.insert(0, 1)
        # nums.append(1)
        # n = len(nums)
        # lookup = [[0 for __ in range(n)] for __ in range(n)]
        
        # maxCoinsRecur(0, n - 1)
        # return lookup[0][n - 1]
        ##DP
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0 for __ in range(n)] for __ in range(n)]
        for k in range(2, n):
            for i in range(0, n - k):
                j = i + k
                for x in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][x] + dp[x][j] + nums[i] * nums[x] * nums[j])
        return dp[0][n - 1]
