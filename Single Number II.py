class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for x in nums:
            one, two = (one & ~x) | (x & ~one & ~two), (two & ~x) | (x & one)
            # tmp = one
            # one = (one & ~x) | (x & ~one & ~two)
            # two = (two & ~x) | (x & tmp) 
        return one
        
        # solution two
        # bits = [0] * 32
        # for a in A:
        #     for i in range(32):
        #         bits[i] += a & 1
        #         a >>= 1
        # ans = 0
        # for i in range(32):
        #     ans += (bits[i] % 3) << i
        # return ans

class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one
#  every element appears 4 times except for one with 2 times
class SolutionEX:
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two