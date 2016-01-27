class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return sum([int(key) for key in bin(n)[2:]])
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count