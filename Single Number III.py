class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_xor_y = reduce(operator.xor, nums, 0)
        ret = [0, 0]
        # -x_xor_y equals ~(x_xor_y - 1)
        bits = x_xor_y & -x_xor_y
        for n in nums:
            # if bits & n:
            #     ret[0] ^= n
            # else:
            #     ret[1] ^= n
            ##int(True) == 1, int(False) == 0
            ##a and b if true, return b, else the first false.
            ret[bool(bits & n)] ^= i
        return ret

class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i
        bit = x_xor_y & ~(x_xor_y - 1)
        x = 0
        for i in nums:
            if i & bit:
                x ^= i
        return [x, x ^ x_xor_y]