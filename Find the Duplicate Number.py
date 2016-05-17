class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            raise Exception('invalid args')
        length = len(nums)
        bits = [0] * 32
        ## from 1 to length - 1
        for i in range(1, length):
            for index in range(32):
                bits[index] += i & 0x01
                i >>= 1
                if i == 0:
                    break
        ## delete 
        for n in nums:
            for index in range(32):
                bits[index] -= n & 0x01
                n >>= 1
                if n == 0:
                    break
        ans = 0
        for c in bits[::-1]:
            ans <<= 1
            if c < 0:
                ans += 1
        return ans
        
        ## anthor solution
        